from django.db import  models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Mensaje(models.Model):
    autor=models.ForeignKey(User,related_name="autor",on_delete=models.CASCADE)
    receptor=models.ForeignKey(User,related_name="receptor",on_delete=models.CASCADE)
    titulo=models.CharField(max_length=100)
    mensaje=RichTextField(blank=True,null=True)
    
    