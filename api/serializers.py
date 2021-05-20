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
