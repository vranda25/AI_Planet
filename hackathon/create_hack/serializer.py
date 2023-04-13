from rest_framework import serializers
from .models import *


class CreateHackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateHack
        fields = '__all__'
