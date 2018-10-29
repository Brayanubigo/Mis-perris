from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.conf import settings


"""
REGIONES= (
    ('Arica y Parinacota', 'Arica y Parinacota'),
    ('Tarapacá', 'Tarapacá'),
    ('Antofagasta', 'Antofagasta'),
    ('Atacama', 'Atacama'),
    ('Coquimbo', 'Coquimbo'),
    ('Valparaíso', 'Valparaíso'),
    ('Metropolitana de Santiago', 'Metropolitana de Santiago'),
    ('Libertador General Bernardo O´Higgins', 'Libertador General Bernardo O´Higgins'),
    ('Maule', 'Maule'),
    ('Ñuble', 'Ñuble'),
    ('Biobío', 'Biobío'),
    ('La Araucanía', 'La Araucanía'),
    ('Los Ríos', 'Los Ríos'),
    ('Los Lagos', 'Los Lagos'),
    ('Aysén del General Carlos Ibáñez del Campo', 'Aysén del General Carlos Ibáñez del Campo'),
    ('Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena'),
    
)

VIVIENDA= (
    ('Casa con patio grande', 'Casa con patio grande'),
    ('Casa con patio pequeño', 'Casa con patio pequeño'),
    ('Casa sin patio', 'Casa sin patio'),
    ('Departamento', 'Departamento'),
)   
"""

class RegistroForm(UserCreationForm):
    User.add_to_class('telefono', models.CharField(max_length=12,null=True)),
    User.add_to_class('rut', models.CharField(max_length=10,null=False)),
    #User.add_to_class('birthday', forms.DateField(widget = forms.SelectDateWidget)),
    User.add_to_class('region', models.CharField(max_length=50, null=False, default='')),
    User.add_to_class('fecha', models.DateTimeField()),
    User.add_to_class('comuna', models.CharField(max_length=30, null=False, default='')),
    User.add_to_class('tipovivienda', models.CharField(max_length=30, null=False, default='')),


    class Meta:
        model = User
        fields = [
                'username',
                'rut',
                'email',
                'telefono',
                'region',
                'fecha',
                'comuna',
                'tipovivienda'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'datepicker'}),
        }
        labels = {
                'username': 'Nombre de usuario',
                'rut': 'Rut',
                'email': 'E-mail',
                'telefono': 'Teléfono',
                'region': 'Region',
                'fecha' :'Fecha',
                'comuna':'Comuna',
                'tipovivienda': 'Tipo vivienda',
        }








