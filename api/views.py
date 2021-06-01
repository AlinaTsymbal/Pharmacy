from django.db.models import Count
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Remedy, Category, RemedySet, MedKit, PharmacyRemedy, Basket, Client, Order
from api.serializers import ShortRemedySerializer, CategorySerializer, RemedySetSerializer, MedKitSerializer, \
    RemedyPharmacySerializer, BasketSerializer, AddToBasketSerializer, ClientSerializer, BasketOrderSerializer, \
    CreateOrderSerializer, OrderSerializer, AdminSerializer


class Me(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = Client.objects.filter(id=request.user.id).first()

        if user is not None:
            return Response(ClientSerializer(user).data, status.HTTP_200_OK)
        else:
            return Response(AdminSerializer(user).data, status.HTTP_200_OK)


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
        return Response(
            RemedyPharmacySerializer(self.model.objects.filter(remedy_id=remedy_id), many=True).data,
            status.HTTP_200_OK
        )


class BasketView(APIView):
    http_method_names = ['get', 'post']
    model = Basket
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(
            BasketSerializer(self.model.objects.get(client__user_id=request.user.id)).data,
            status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = AddToBasketSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        basket = self.model.objects.filter(client_id=request.user.id).first()
        if basket is None:
            basket = self.model.objects.create(client=Client.objects.get(id=request.user.id))

        remedy = basket.basket_remedies.filter(remedy_id=serializer.data.get('remedy')).first()

        if remedy is not None:
            remedy.amount += 1
            remedy.save()
        else:
            basket.basket_remedies.create(remedy_id=serializer.data.get('remedy'))

        return Response(BasketSerializer(basket).data, status.HTTP_200_OK)


class OrderView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(BasketOrderSerializer(Basket.objects.get(client_id=request.user.id)).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)

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
            OrderSerializer(Order.objects.filter(client_id=request.user.id), many=True).data,
            status.HTTP_200_OK,
        )
