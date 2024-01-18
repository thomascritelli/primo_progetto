from django.shortcuts import render
def getMaterie():
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    return materie

def getDiz():
    diz= {'Giuseppe Gullo':[('Matematica',9,0),('Italiano',7,3),('Inglese',7.5,4),('Storia',7.5,4),('Geografia',5,7)],'Antonio Barbera':[('Matematica',8,1),('Italiano',6,1),('Inglese',9.5,0),('Storia',8,2),('Geografia',8,1)],'Nicola Spina':[('Matematica',7.5,2),('Italiano',6,2),('Inglese',4,3),('Storia',8.5,2),('Geografia',8,2)]}
    return diz

def view_a(request):
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    context = {
        'materie':materie,
    }
    return render(request, "view_a.html", context)



def view_b(request):
    context = {
        'voti': getDiz(),
    }
    return render(request, 'view_b.html', context)

def view_c(request):
    medie = {}
    for chiave, valori in getDiz().items():
        media = 0
        for materia,voto,assenze in valori:
            media += voto
        medie[chiave] = media / len(valori)
    context = {
        'medie': medie,
    }
    return render(request, 'view_c.html', context)

def view_d(request):
    min_max = {}

    max = 0
    max_materia = ""
    max_studente = ""
    min = 0

    for chiave, valori in getDiz().items():
        for materia,voto,assenze in valori:
            if (voto > max):
                if min == 0:
                    min = voto
                    min_materia = materia
                    min_studente = chiave
                max = voto
                max_materia = materia
                max_studente = chiave
            elif voto < min:
                min = voto
                min_materia = materia
                min_studente = chiave

    min_max[min_studente] = [(min_materia,min)]
    min_max[max_studente] = [(max_materia,max)]

    context = {
        'min_max' : min_max,
    }
    return render(request, 'view_d.html', context)


