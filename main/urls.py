from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('guia/', views.guia, name='guia'),
    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('guia_derivadas/', views.guia_derivadas,name='guia_derivadas'),
    path('guia_optimizacion/', views.guia_optimizacion,name='guia_optimizacion'),
    path('ejercicios_derivadas/', views.ejercicios_derivadas,name='ejercicios_derivadas'),
]