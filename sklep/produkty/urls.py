from django.urls import path
from .views import dodaj_produkt, lista_produktow

urlpatterns = [
    path('', lista_produktow, name='lista_produktow'), 
    path('dodaj/', dodaj_produkt, name='dodaj_produkt'),
]
