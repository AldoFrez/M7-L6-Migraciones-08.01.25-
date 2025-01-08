from django.shortcuts import render
from django.shortcuts import render
from .models import Autor, Libro

def index(request): # va a pasar get all dos tablas autor y libro y las pasa en un contexto, en una misma vista
    autores = Autor.objects.all()
    libros = Libro.objects.all()
    context = {
        'autores': autores,
        'libros': libros
    }
    print (context['autores'][0].email)
    return render(request, 'modelos/index.html', context)
# Create your views here.
