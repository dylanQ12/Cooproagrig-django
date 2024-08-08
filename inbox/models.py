from django.db import models

class Inbox(models.Model):
    nombre = models.CharField(max_length=260)
    email = models.EmailField(max_length=280)
    mensaje = models.TextField()
    fecha_enviado = models.DateTimeField(auto_now_add=True)
    
