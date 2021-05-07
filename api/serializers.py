from rest_framework import serializers

from api.models import Remedy, Category


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
            'name',
            'description',
        ]
