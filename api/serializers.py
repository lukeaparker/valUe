from rest_framework.serializers import ModelSerializer

from value_app.models import Value

class ValueSerializer(ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


