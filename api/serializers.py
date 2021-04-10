from rest_framework import serializers

from api.models import Remedy


class ShortRemedySerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedy
        fields = [
            'name',
            'description',
        ]
