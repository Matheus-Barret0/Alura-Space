from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Arquivo responsavel por exibir informações na tela

def index(request):
    return render(request, 'index.html')