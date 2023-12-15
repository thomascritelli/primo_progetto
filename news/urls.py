from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('homeview', homeview, name = 'homeview'),
    path('articoli/<int:pk>', articoloDetailView, name = 'articolo_detail'),
    path('lista_articoli/<int:pk>', lista_articoli, name = 'lista_articoli'),
    path('lista_articoli/', lista_articoli, name = 'lista_articoli'),
]
