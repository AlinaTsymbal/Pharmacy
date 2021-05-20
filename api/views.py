from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Remedy, Category, RemedySet, MedKit, PharmacyRemedy
from api.serializers import ShortRemedySerializer, CategorySerializer, RemedySetSerializer, MedKitSerializer, \
    RemedyPharmacySerializer


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
