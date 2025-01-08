from django.db import models

# Modelo para demostración
class Autor(models.Model): # una clase , es una POO, se definen los obj segun su clase, la heredear models.Model, hace que se convierta a tabla tipo excel, el ID lo asume django asiq ue el segundo campo es nombre ye tercero es email
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self): # en caso de dar permiso al administrador, es para que el pueda  verla con l oespecificado en el return
        return self.nombre # el usuario admin cuando entre por el panel de admin vera el autor por su nombre


class Libro(models.Model): # se crea una clase libro, que hereda de models.Model
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # trae uan FK de la tabla autor, y se le dice que si se borra el autor se borra el libro

    def __str__(self):
        return self.titulo

# Create your models here.
