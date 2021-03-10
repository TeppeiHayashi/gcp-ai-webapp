from libs.gcp.base_client import GcpBaseClient
from libs.gcp.vision.response import VisionApiResponse

# Imports the Google Cloud client library
from google.cloud import vision


class VisionApiClient(GcpBaseClient):
    
    def __init__(self):
        super().__init__()
        self.client = vision.ImageAnnotatorClient()
            
    def sendRequest(self, type, content):        
        try:
            image = vision.Image(content=content)
            # レスポンス取得
            response = getattr(self.client, type)(image=image)
            response = VisionApiResponse(response, type, content)
                        
            return response
    
        except Exception as e:
            print("exception in {0}, {1}".format("call_api", e))
            raise(e)
    
