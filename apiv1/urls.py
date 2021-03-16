from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.vision.RequestViewSet)


app_name = 'apiv1'
urlpatterns = [
    path('vision/<type_name>/', include(router.urls)),
]