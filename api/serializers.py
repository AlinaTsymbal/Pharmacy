import base64
import os

from rest_framework import serializers

from api.models import Remedy, Category, RemedySet, MedKit, PharmacyRemedy, Pharmacy, Basket


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
        print(os.getcwd())

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
