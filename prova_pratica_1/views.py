from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "prova_pratica_home.html")

def somma(request):
    var1 = random.randint(1,10)
    var2 = random.randint(1,10)
    context = {
        'var1' : var1,
        'var2' : var2,
        'sum' : var1 + var2,
    }
    return render(request, "maxmin.html", context)

def media(request):
    lista = []
    somma = 0
    for i in range(30):
        lista.append(random.randint(1,10))
        somma += lista[i]
    somma /= 30
    context = {
        'lista' : lista,
        'media' : somma.__round__(0),
    }
    return render(request, "media.html", context)

def voti(request):
    voti ={'Aldo':8, 'Giovanni':7, 'Giacomo':5 }
    context = {
        'voti' : voti
    } 
    return render(request, "voti.html", context)
