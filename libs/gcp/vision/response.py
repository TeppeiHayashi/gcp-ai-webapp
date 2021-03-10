import cv2
import numpy as np
from PIL import Image
from io import BytesIO

from google.protobuf.json_format import MessageToJson

class VisionApiResponse:
     
    def __init__(self, response, type, content):
        self.__response = response
        self.type = type
        self.content = content

    def json(self):
        return MessageToJson(self.__response._pb)
    
    
    def result_content(self):
        return getattr(self, f'result_content_{self.type}')()
        
        
    def result_content_object_localization(self):
        # 画像をOpenCVで読み込む
        img = cv2.imdecode(np.frombuffer(self.content, np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR→RGBに変換
    
        img2 = img.copy()
        h, w = img2.shape[0:2]
        color = (255, 0, 0)
        font = cv2.FONT_HERSHEY_DUPLEX
    
        for obj in self.__response.localized_object_annotations:
            # バウンディングボックスの左上と右下の角の座標を取得して書き足す
            box = [(v.x * w, v.y * h) for v in obj.bounding_poly.normalized_vertices]

            cv2.rectangle(img2, tuple(map(int, box[0])), tuple(map(int, box[2])), color, 2)
            # オブジェクトの名前を取得して書き足す
            obname = obj.name
            cv2.putText(img2, obname ,tuple(map(int, box[3])), font, 
                        1, color)
    
        img2 = Image.fromarray(img2)
        image_io = BytesIO()
        img2.save(image_io, format="JPEG")
        return image_io
    
