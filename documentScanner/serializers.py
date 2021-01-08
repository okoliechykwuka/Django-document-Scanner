from rest_framework import serializers
from .models import ImageScanner
from django.contrib.auth.models import User
 

class ImageScannerSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = ImageScanner
        fields = ['id', 'name', 'ImageFile']
    
    def create(self, validated_data):
        return ImageScanner.objects.create(**validated_data)
