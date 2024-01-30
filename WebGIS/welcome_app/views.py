from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio (request):
    #return HttpResponse("Testando a minha view")
    return render(request, 'index.html')