from django.shortcuts import render


# Create your views here.
def index(request):
    
    contexto = {'hola'}
    return render(request, 'main/index.html', contexto)
# Create your views here.
