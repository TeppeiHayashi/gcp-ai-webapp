from django.contrib import admin

from image_recognition.models import Request, Type

class RequestModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'result', 'json','created_at')
    
admin.site.register(Request, RequestModelAdmin)
admin.site.register(Type)