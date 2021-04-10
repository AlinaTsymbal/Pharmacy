# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    http_method_names = ['get']

    def get(self, response=Response()):
        return response
