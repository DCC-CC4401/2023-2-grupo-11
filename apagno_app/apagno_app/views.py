from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, este es un testeo")