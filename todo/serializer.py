from rest_framework.exceptions import *
from .models import *
from rest_framework.serializers import ModelSerializer

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__' # id ism