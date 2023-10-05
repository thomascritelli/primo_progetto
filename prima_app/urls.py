from django.urls import path
from prima_app.views import *

app_name = "prima_app"
urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('', welcome, name = 'welcome'),
    path('', chi_siamo, name = 'chi_siamo'),
    path('', lista, name = 'lista')
]