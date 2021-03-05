from rest_framework import serializers
from image_recognition.models import Request

class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = '__all__'