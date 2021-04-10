from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Remedy
from api.serializers import ShortRemedySerializer


class RemediesView(APIView):
    http_method_names = ['get']

    def get(self, request):
        categories = request.query_params.getlist('category', None)

        remedies = Remedy.objects.all()

        if categories is not None:
            remedies = remedies.filter(categories__in=categories) \
                .annotate(cnt=Count('categories')).filter(cnt=2)

        return Response(ShortRemedySerializer(remedies, many=True).data, status.HTTP_200_OK)
