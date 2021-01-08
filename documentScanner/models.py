from django.db import models
from datetime import date
import cv2
import tempfile
from django.utils import timezone
import os
from .scan import Scanner
import numpy as np
from PIL import Image

# Create your models here.
def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    return f"ScannedImage/{now:%Y-%m-%d %H-%M}/{instance.id}/{filename}"




class ImageScanner(models.Model):
    ImageFile = models.ImageField(upload_to= upload_to)
    name= models.CharField(max_length=500)
    
    

    def __str__(self):
        return self.name + ": " + str(self.ImageFile)

    def save(self, *args, **kwargs):
        super(ImageScanner, self).save(*args, **kwargs)
        
        # image = np.asarray(bytearray(self.ImageFile.read()), dtype="uint8")
        # image = cv2.imdecode(image, cv2.IMREAD_COLOR) 
        #open image
        pil_img = Image.open(self.ImageFile)
        cv_img = np.array(pil_img)
        Img = Scanner(cv_img)
        


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


_UNSAVED_FILEFIELD = 'unsaved_filefield'

@receiver(pre_save, sender=ImageScanner)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.ImageFile)
        instance.ImageFile = None

@receiver(post_save, sender=ImageScanner)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.ImageFile = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save() 