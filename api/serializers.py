import base64
import os

from rest_framework import serializers

from api.models import Remedy, Category, RemedySet, MedKit


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
