from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'inicio'),
    path("acerca/", views.acerca, name="acerca"),
    path("temario/",views.temario,name = "temario"),
    path('pato', views.pato, name = 'pato'),
    path('tarea2/', views.tarea2, name = 'tarea2')
]