from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Remedy, Category, RemedySet, MedKit, PharmacyRemedy, Basket, Client, Order, Admin, AuthUser
from api.serializers import ShortRemedySerializer, CategorySerializer, RemedySetSerializer, MedKitSerializer, \
    RemedyPharmacySerializer, BasketSerializer, AddToBasketSerializer, ClientSerializer, BasketOrderSerializer, \
    CreateOrderSerializer, OrderSerializer, AdminSerializer, RemedySerializer, RegistrationSerializer


class Me(APIView):
    http_method_names = ['get', 'post', 'patch']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = Client.objects.filter(user_id=request.user.id).first()

        if user is not None:
            return Response(ClientSerializer(user).data, status.HTTP_200_OK)
        else:
            return Response(
                AdminSerializer(Admin.objects.filter(user_id=request.user.id).first()).data,
                status.HTTP_200_OK
            )

    def patch(self, request):
        user = Client.objects.get(user_id=request.user.id)
        user.phone = request.data.get('phone')
        user.address = request.data.get('address')
        user.user.first_name = request.data.get('first_name')
        user.user.last_name = request.data.get('last_name')
        user.user.email = request.data.get('email')
        user.user.save()

        user.save()

        return Response(ClientSerializer(user).data, status.HTTP_200_OK)


class Categories(APIView):
    http_method_names = ['get']

    def get(self, request):
        return Response(CategorySerializer(Category.objects.all(), many=True).data, status.HTTP_200_OK)


class RemediesView(APIView):
    http_method_names = ['get']

    def get(self, request):
        categories = request.query_params.getlist('category', None)

        remedies = Remedy.objects.all()

        if categories is not None and len(categories) > 0:
            remedies = remedies.filter(categories__in=map(int, categories)) \
                .annotate(cnt=Count('categories')).filter(cnt=len(categories))

        return Response(ShortRemedySerializer(remedies, many=True).data, status.HTTP_200_OK)


class RemedySets(APIView):
    http_method_names = ['get']

    def get(self, request):
        return Response(RemedySetSerializer(RemedySet.objects.all(), many=True).data, status.HTTP_200_OK)


class MedKits(APIView):
    http_method_names = ['get']

    def get(self, request):
        return Response(MedKitSerializer(MedKit.objects.all(), many=True).data, status.HTTP_200_OK)


class RemedyDetails(APIView):
    http_method_names = ['get']
    model = PharmacyRemedy

    def get(self, request, remedy_id):
        get_details = request.query_params.get('details', False)
        if not get_details:
            return Response(
                RemedyPharmacySerializer(self.model.objects.filter(remedy_id=remedy_id), many=True).data,
                status.HTTP_200_OK
            )

        return Response(
            RemedySerializer(Remedy.objects.get(id=remedy_id)).data,
            status.HTTP_200_OK
        )


class BasketView(APIView):
    http_method_names = ['get', 'post', 'patch']
    model = Basket
    permission_classes = (permissions.IsAuthenticated,)

    def add_remedy(self, basket, remedy_id):
        remedy = basket.basket_remedies.filter(remedy_id=remedy_id).first()

        if remedy is not None:
            remedy.amount += 1
            remedy.save()
        else:
            basket.basket_remedies.create(remedy_id=remedy_id)

        return basket

    def get(self, request):
        if request.user.type == 'ADMIN':
            return Response(status.HTTP_403_FORBIDDEN)
        basket = self.model.objects.filter(client_id=request.user.id).first()
        if basket is None:
            basket = self.model.objects.create(client=Client.objects.get(user_id=request.user.id))
        return Response(
            BasketSerializer(basket).data,
            status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = AddToBasketSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        basket = self.model.objects.filter(client_id=request.user.id).first()
        if basket is None:
            try:
                basket = self.model.objects.create(client=Client.objects.get(user_id=request.user.id))
            except:
                return Response(status=status.HTTP_403_FORBIDDEN)
        remedy_data = request.data.get('remedy', None)
        remedies_data = request.data.get('remedies', None)

        if remedy_data is not None:
            self.add_remedy(basket, remedy_data)

            return Response(BasketSerializer(basket).data, status.HTTP_200_OK)
        if remedies_data is not None:
            for r in remedies_data:
                self.add_remedy(basket, r)
            return Response(BasketSerializer(basket).data, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        basket = self.model.objects.filter(client_id=request.user.id).first()
        if basket is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        record_id = request.data.get('id', None)

        if record_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.query_params.get('delete', False):
            basket.basket_remedies.filter(id=record_id).delete()

            return Response(BasketSerializer(basket).data, status.HTTP_200_OK)
        if request.query_params.get('replace', False):
            remedy_id = request.data.get('remedy')
            basket_remedy = basket.basket_remedies.filter(id=record_id).first()
            new_remedy = basket.basket_remedies.filter(remedy_id=remedy_id).first()

            if new_remedy is not None:
                new_remedy.amount += 1
                new_remedy.save()
                basket_remedy.delete()
            else:
                basket_remedy.remedy_id = remedy_id
                basket_remedy.save()

            return Response(BasketSerializer(basket).data, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(BasketOrderSerializer(Basket.objects.get(client_id=request.user.id)).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        Basket.objects.get(client_id=request.user.id).delete()

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(client_id=request.user.id)

        for r in serializer.validated_data.get('remedies'):
            order.order_remedies.create(
                remedy_id=r.get('remedy').id,
                pharmacy_id=r.get('pharmacy').id,
                amount=r.get('amount')
            )

        return Response(status=status.HTTP_200_OK)


class ListOrder(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(
            OrderSerializer(Order.objects.all(), many=True).data,
            status.HTTP_200_OK,
        )


class Registration(APIView):
    http_method_names = ['post']
    model = AuthUser
    serializer = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        username = serializer.data.get('username')
        password = make_password(serializer.data.get('password'))

        user = self.model.objects.create(
            username=username,
            password=password,
            first_name="Ім'я не вказано",
            last_name="Прізвище не вказано",
        )

        client = Client()
        client.user = user

        client.save()

        return Response(ClientSerializer(client).data, status.HTTP_200_OK)


class CloseOrder(APIView):
    http_method_names = ['post']
    model = Order

    def post(self, request):
        order = self.model.objects.get(id=request.data.get('orderId'))

        order.resolved_at = timezone.now()
        order.save()

        return Response(OrderSerializer(self.model.objects.all(), many=True).data, status.HTTP_200_OK)
