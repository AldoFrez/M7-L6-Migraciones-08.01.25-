import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraciones.settings')
django.setup()

from modelos.models import Autor, Libro
from datetime import date

def poblar_datos():
    autor1 = Autor.objects.create(nombre="Jane Austen", email="jane.austen@example.com")
    autor2 = Autor.objects.create(nombre="George Orwell", email="george.orwell@example.com")

    Libro.objects.create(titulo="Pride and Prejudice",fecha_publicacion=date(1813, 1, 28), autor=autor1)
    Libro.objects.create(titulo="1984",fecha_publicacion=date(1949, 6, 8), autor=autor2)
    Libro.objects.create(titulo="Emma",fecha_publicacion=date(1815, 12, 23), autor=autor1)

    print("Datos iniciales cargados con éxito.")

if __name__ == "__main__":
    poblar_datos()