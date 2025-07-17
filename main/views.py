from django.shortcuts import render
# Create your views here.
def index(request):  
    return render(request, 'main/index.html')

def guia(request): 
    return render(request, 'main/guia.html')

def ejercicios(request):
    return render(request, 'main/ejercicios.html')

def guia_derivadas(request):
    return render(request, 'main/guia_derivadas.html')
def guia_optimizacion(request):
    return render(request,'main/guia_optimizacion.html')
def ejercicios_derivadas(request):
    return render(request,'main/ejercicios_derivadas.html')