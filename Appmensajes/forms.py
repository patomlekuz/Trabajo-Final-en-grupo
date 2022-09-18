from pyexpat import model
from django import forms
from Appmensajes.models import Mensaje
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ContenidoMensaje(forms.ModelForm):
    titulo=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    

    class Meta:
        model=Mensaje
        fields=("receptor","titulo","mensaje")
      


    