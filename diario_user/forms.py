from django.forms import ModelForm, DateInput
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ['user', 'nombre_completo', 'apellidos', 'fecha_nacimiento', 'email']

        labels = {
            'user': 'Usuario',
            'nombre_completo': 'Nombre completo del usuario',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'email': 'Correo electrónico',
        }

        widgets = {
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
        }

        
class DiaryEntries(ModelForm):
    class Meta:
        model = DiarioMiki

        fields = ['user', 'titulo', 'contenido']

        labels = {
            'user': 'Usuario',
            'titulo': 'Título de la entrada',
            'contenido': 'Contenido de la entrada',
        }