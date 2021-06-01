import base64

from rest_framework import serializers

from api.models import Remedy, Category, RemedySet, MedKit, PharmacyRemedy, Pharmacy, Basket, Client, BasketRemedy


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class ShortRemedySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super(ShortRemedySerializer, self).to_representation(instance)

        try:
            with open(f'./api/images/{instance.id}', 'rb') as image:
                image_base64 = base64.b64encode(image.read())

            data['image'] = image_base64
        except FileNotFoundError as e:
            print(e)
        return data

    class Meta:
        model = Remedy
        fields = [
            'id',
            'name',
            'description',
        ]


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = [
            'id',
            'address',
            'name',
        ]


class RemedyPharmacySerializer(serializers.ModelSerializer):
    remedy = ShortRemedySerializer()
    pharmacy = PharmacySerializer()

    class Meta:
        model = PharmacyRemedy
        fields = [
            'id',
            'remedy',
            'pharmacy',
            'price'
        ]


class RemedySetSerializer(serializers.ModelSerializer):
    remedies = ShortRemedySerializer(many=True)

    class Meta:
        model = RemedySet
        fields = [
            'id',
            'name',
            'description',
            'remedies',
        ]


class MedKitSerializer(serializers.ModelSerializer):
    remedies = ShortRemedySerializer(many=True)

    class Meta:
        model = MedKit
        fields = [
            'id',
            'name',
            'description',
            'remedies',
        ]


class BasketSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(BasketSerializer, self).to_representation(instance)

        remedies = []

        for br in instance.basket_remedies.all():
            remedies.append(
                {
                    'id': br.remedy.id,
                    'name': br.remedy.name,
                    'amount': br.amount,
                    'pharmacy': br.pharmacy
                }
            )

        data['remedies'] = remedies

        return data

    class Meta:
        model = Basket
        fields = [
            'id',
        ]


class AddToBasketSerializer(serializers.Serializer):
    remedy = serializers.PrimaryKeyRelatedField(queryset=Remedy.objects.all(), required=True)
    amount = serializers.IntegerField(default=1, required=False)
    pharmacy = serializers.PrimaryKeyRelatedField(queryset=Pharmacy.objects.all(), required=False)

    class Meta:
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super(OrderItemSerializer, self).to_representation(instance)

        remedy = ShortRemedySerializer(instance.remedy).data

        pharmacy_set = instance.remedy.pharmacyremedy_set.all()

        data['name'] = remedy.get('name')
        data['pharmacy'] = instance.remedy.pharmacyremedy_set.first().pharmacy.id
        data['pharmacies'] = PharmacySerializer([p.pharmacy for p in pharmacy_set], many=True).data
        for (i, p) in enumerate(pharmacy_set):
            data['pharmacies'][i]['price'] = p.price
        del data['remedy']

        return data

    class Meta:
        model = BasketRemedy
        fields = '__all__'


class BasketOrderSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super(BasketOrderSerializer, self).to_representation(instance)

        remedies = OrderItemSerializer(instance.basket_remedies, many=True).data
        data['remedies'] = remedies

        return data

    class Meta:
        model = Basket
        fields = '__all__'
