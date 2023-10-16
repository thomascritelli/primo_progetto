from django.shortcuts import render
import datetime

# Create your views here.
def seconda_app(request):
    return render(request, "seconda_app.html")

def es_if(request):
    context = {
        'var1' : 200,
        'var2' : 200,
        'var3' : 300,
    }
    return render(request, "es_if.html", context)

def if_else_elif(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    return render(request, "if_else_elif.html", context)

def es_for(request):
    context = {
        'list1' : [1, datetime.date(2023,10,16), 'Oggi farò il quinto nome di un top di serie A dentro la questione del calcioscomesse!'],
        'list2' : [1, datetime.date(2023,10,16), 'Ho almeno una 50 di nomi'],
        'my_dict' : {'chiave1':'Valore1', 'chiave2':'Valore2'},
    }
    return render(request, "es_for.html", context)