from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Contacto


class ContactoForm(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['gmail', 'nombre', 'apellido', 'categoria', 'numero' , 'comentario']
        labels ={
            'gmail': 'Correo Electrónico:', 
            'nombre': 'Nombre:', 
            'apellido': 'Apellido:', 
            'categoria': 'Categoría:',
            'numero': 'Numero:',
            'comentario': 'Comentario:',
        }
        widgets={
            'gmail': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo Electrónico', 
                    'id': 'gmail',
                    'name': 'gmail',
                    'type': 'email',
                    
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre',
                    'name': 'nombre',
                    'onchange': 'CambiarMayusculasNombre()',
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido',
                    'name': 'apellido',
                    'onchange': 'CambiarMayusculasApellido()',
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                    'name': 'categoria'
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese numero', 
                    'id': 'numero',
                    'name': 'numero',
                    'type': 'number'
                }
            ),
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comentario', 
                    'id': 'comentarios',
                    'name': 'comentario',
                    'rows': '5',
                }
            ), 


        }