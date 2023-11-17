from django.http import *
from django.shortcuts import *
from .models import *
# Create your views here.
def homeview(request):
    """
    # Concatenazione degli elementi
    a = ""
    g = ""
    
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + "<br>Giornalisti:<br>" + g
    return HttpResponse(f"<h1>{response}</h1>")
    """

    """
    # Utilizzo degli array per contenere gli elementi
    a = []
    g = []

    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    
    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse(f"<h1>{response}</h1>")
    """


    # Utilizzo di un dizionario per contenere gli elementi
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    return render(request, "news_homepage.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk = pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)