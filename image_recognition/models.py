import uuid
import json
from django.db import models

'''
Fileのアップロード先のパスを返す
'''
def upload_path(instance, filename):
    return f'{instance.type.name}/{instance.id}/{filename}'


'''
検証用画像はファイル名をすべて　'target.[拡張子]' にする。
'''  
def target_upload_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'target.{ext}'
    return upload_path(instance, filename)


class Type(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True, 
        null=False, 
        verbose_name="検証名",
    )
    
    def __str__(self):
        return self.name


class Request(models.Model):
    
    class Meta:
        ordering = ['-created_at']
    
    id = models.UUIDField(
        primary_key=True, 
        default=str(uuid.uuid4()).replace('-', ''), 
        editable=False,
    )
    
    type = models.ForeignKey(
        Type,
        null=False,
        on_delete=models.PROTECT,
    )
    
    target = models.FileField(
        upload_to=target_upload_path, 
        blank=False, 
        null=False,
        verbose_name='検証用ファイル'
    )
    
    result = models.FileField(
        upload_to=upload_path,
        default=None,
        verbose_name='検証結果',
    )
    
    json = models.FileField(
        upload_to=upload_path,
        default=None,
        verbose_name='レスポンスJSON',
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日',
    )
    
    '''
    JSONの内容を返す
    '''
    def json_content(self):
        f = self.json.open()
        content = json.load(f)
        f.close()
        return content
    
    def __str__(self):
        return f'{self.type.name}_{self.created_at}'
    
    
    '''
    Fileを格納するDirectoryにIDを用いるため、save()をオーバーライド
    '''
    def save(self, *args, **kwargs):
        # 新規登録時はまだIDを持っていない
        if self.id is None:
            tmp = [self.target, self.result, self.json]
            
            # 一度空でデータを登録
            self.target = self.result = self.json = None
            super().save(*args, **kwargs)
            
            # レコード（ID)作成後、保持していたデータを格納
            self.target, self.result, self.json = tmp
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")         
        
        super().save(*args, **kwargs)
    