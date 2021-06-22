from django.shortcuts import redirect, render
from .models import Contacto 
from .forms import ContactoForm

# Create your views here.

def home(request):

    return render(request, 'home.html', )


def quienesSomos(request):

    return render(request, 'quienessomos.html', )


def crearContacto(request):
    contactos = Contacto.objects.all()
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('home')
    else:
        contacto_form= ContactoForm()
    return render(request, 'AllStars/form_crearconsulta.html', {'contacto_form': contacto_form, 'datos':contactos})


def ventaArticulos(request):

    return render(request, 'galeriadefotos.html')


def form_modificarconsulta(request,id):
    contactos = Contacto.objects.get(gmail=id)

    datos={
        'form':ContactoForm(instance=contactos)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance = contactos)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')
    return render(request, 'AllStars/form_modificarconsulta.html',datos)


def form_borrarconsulta(request,id):
    contactos = Contacto.objects.get(gmail=id)
    contactos.delete()
    return redirect('home')