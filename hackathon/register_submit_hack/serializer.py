from rest_framework import serializers
from .models import *


class RegisterHackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResigterHack
        fields = '__all__'

class UploadSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadSubmission
        fields = '__all__'
