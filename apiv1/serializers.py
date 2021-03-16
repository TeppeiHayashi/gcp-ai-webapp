from rest_framework import serializers
from image_recognition.models import Request, Type

class RequestSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Request
        fields = ['id', 'type', 'target', 'result', 'json', 'created_at','json_content']


class TypeSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True)
    class Meta:
        model = Type
        fields = ['id', 'name', 'requests']
    
