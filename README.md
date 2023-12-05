# WebPlanner: Plataforma de Gestión de Proyectos y Tareas en Django

Este proyecto ha sido fundamental para adquirir un entendimiento sólido de los conceptos básicos en Django. 
La visión es desarrollar una plataforma web que posibilite la creación y gestión de proyectos y tareas. En este contexto, un proyecto puede contener múltiples tareas, estableciendo así una relación donde cada tarea está vinculada a un proyecto específico.
Durante su desarrollo, exploramos a fondo el funcionamiento de modelos, vistas, y URLs, así como el proceso de realización de migraciones.

Asimismo, profundizamos en la integración de contenido dinámico en HTML desde el Back-End mediante el uso de Jinja2, y aprendimos a trabajar con archivos estáticos de manera efectiva.

Otro aspecto clave de nuestro aprendizaje fue la creación de formularios mediante código en Python, lo que amplió nuestras habilidades para manejar la entrada de datos. A continuación, se presentan algunos ejemplos de código que ilustran estas funcionalidades:

- Modelo en Django:
  ```Python
  # models.py
  
  from django.db import models
  
  class Producto(models.Model):
      nombre = models.CharField(max_length=50)
      precio = models.DecimalField(max_digits=5, decimal_places=2)
  
      def __str__(self):
          return self.nombre
  ```
  
- Vistas en Django:
  ```Python
  # views.py
  
  from django.shortcuts import render
  from .models import Producto
  
  def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})
    ```

  
- URLs en Django:
  ```Python
    # urls.py
    
    from django.urls import path
    from .views import lista_productos
    
    urlpatterns = [
      path('productos/', lista_productos, name='lista_productos'),
      # Otros patrones de URL aquí...
    ]
  ```

  
- Plantilla HTML con Jinja2:
  ```HTML
  <!-- lista_productos.html -->
  
  <ul>
    {% for producto in productos %}
      <li>{{ producto.nombre }} - {{ producto.precio }}</li>
    {% endfor %}
  </ul>
  ```

  
- Formulario en Django:
  ```Python
  # forms.py

  from django import forms
  from .models import Producto
  
  class ProductoForm(forms.ModelForm):
      class Meta:
          model = Producto
          fields = ['nombre', 'precio']
  ```


- Uso del Panel de Administrador de Django:
  ```Python
  # admin.py
  
  from django.contrib import admin
  from .models import Producto
  
  admin.site.register(Producto)
  ```
