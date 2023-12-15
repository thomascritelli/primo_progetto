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

# def view_c(request):
#     media = 0
#     valoriMedia = [("(getDiz()[0]",0),("Antonio Barbera",0),("",0)]

#     cont = 0
#     for valori in (getDiz()):
#         media = 0
#         for i in range(len(getMaterie())):
#             media += valori[1][i]
#         media /= cont
#         valoriMedia[cont][1] = media
#         cont += 1
        
            
#     context = {
#         'voti': getDiz(),
#         'valoriMedia':valoriMedia,
#     }
#     return render(request, 'view_c.html', context)

# def view_d(request):
#     max = 0
#     min = max
#     for i in range(len(getDiz())):
#         for j in range(len(getMaterie())):
#             if (getDiz()[i][j][1] > max):
#                 max = getDiz()[i][j][1]
#             elif getDiz()[i][j][1] < min:
#                 min = getDiz()[i][j][1]
#     valoriMedia = [(getDiz()[i],max,min),(getDiz()[i],max,min),(getDiz()[i],max,min)]


