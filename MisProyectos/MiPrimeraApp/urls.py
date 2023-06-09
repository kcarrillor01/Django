from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('presentacion', views.presentacion, name='presentacion'),
    path('libros', views.libros, name='libros'),
    path('crear', views.crear, name='crear'),
    path('editar', views.editar, name='editar'),
    path('eliminar/<int:idParametro>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:idParametro>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT )