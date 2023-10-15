from django.contrib import admin
from django.urls import path, include
from seconda_app.views import *

app_name = "seconda_app"

urlpatterns = [
    path('seconda_app', seconda_app, name = 'seconda_app'),
    path('es_if', es_if, name = 'es_if'),
    path('if_else_elif', if_else_elif, name = 'if_else_elif'),
]