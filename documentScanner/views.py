from .models import ImageScanner
from .serializers import ImageScannerSerializer
from rest_framework import viewsets


class ImageScannerView(viewsets.ModelViewSet):
    queryset = ImageScanner.objects.all()
    serializer_class = ImageScannerSerializer
