from django import forms
from .models import Post
from .models import Perros_Rescatados

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )

class Perro_RescatadoForm(forms.ModelForm):
	class Meta:
		model=Perros_Rescatados
		fields=('foto_perro','nombre_perro' , 'raza_predominante' , 'descripcion','estado', )