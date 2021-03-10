from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from image_recognition.models import Request, Type
from .serializers import RequestSerializer

from libs.gcp.vision.client import VisionApiClient

class RequestViewSet(viewsets.ModelViewSet):
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        
        data = request.data
        serializer = RequestSerializer(data=data, context={'request': request})
        
        if serializer.is_valid():
            # 検証画像を取得
            content = data['target'].read()
            # 検証種類
            type_name = Type.objects.get(pk=data['type']).name
            
            # GCPクライアントの作成
            client = VisionApiClient() 
            # リクエストの送信
            response = client.sendRequest(
                content = content,
                type = type_name,
            )
            data['json'] = ContentFile(response.json(), 'response.json')
            result_content = response.result_content()
            data['result'] = InMemoryUploadedFile(result_content, None, 'result.jpg',"image/jpeg", result_content.getbuffer().nbytes, None)
            
            serializer = RequestSerializer(data=data, context={'request': request})
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)