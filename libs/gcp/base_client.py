import os
from django.conf import settings


class GcpBaseClient:    
    def __init__(self):
        # OSの環境変数設定
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']=settings.GOOGLE_APPLICATION_CREDENTIALS
        