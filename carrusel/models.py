from django.db import models
import os
from django.conf import settings


# Create your models here.
class Carousel(models.Model):
    foto = models.ImageField(upload_to="img_carousel/")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Carousel.objects.get(pk=self.pk)
            if old_instance.foto and self.foto != old_instance.foto:
                if os.path.isfile(old_instance.foto.path):
                    os.remove(old_instance.foto.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
