from django.db import models
import os


class Opinion(models.Model):
    foto = models.ImageField(upload_to="img_opinions/")
    nombre_completo = models.CharField(max_length=285)
    comentario = models.TextField()

    def __str__(self):
        return f"{self.nombre_completo} - {self.comentario}"

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Opinion.objects.get(pk=self.pk)
            if old_instance.foto and self.foto != old_instance.foto:
                if os.path.isfile(old_instance.foto.path):
                    os.remove(old_instance.foto.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
