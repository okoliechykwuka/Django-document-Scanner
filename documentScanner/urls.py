from django.urls import path, include
from .views import ImageScannerView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'documentScanner', ImageScannerView)

urlpatterns = [
    path('', include(router.urls)),
    
    
]