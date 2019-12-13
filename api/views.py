from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from value_app.models import Value
from api.serializers import ValueSerializer

class ValueList(APIView):
    def get(self, request):
        values = Value.objects.all()[:20]
        data = ValueSerializer(values, many=True).data
        return Response(data)


