from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    return HttpResponse ("<h1>hola mundo</h1>")

def home (request):
    return render(request, 'index.html')