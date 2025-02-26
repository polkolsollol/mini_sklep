from django.shortcuts import render, redirect
from .models import Produkt
from .forms import ProduktForm

# Widok do wyświetlania listy produktów
def lista_produktow(request):
    produkty = Produkt.objects.all()  # Pobieramy wszystkie produkty z bazy danych
    return render(request, 'produkty/lista.html', {'produkty': produkty})

# Widok do dodawania nowych produktów
def dodaj_produkt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()  # Zapisujemy produkt do bazy
            return redirect('lista_produktow')  # Po zapisaniu produktu przekierowujemy na stronę z listą produktów
    else:
        form = ProduktForm()

    return render(request, 'produkty/dodaj_produkt.html', {'form': form})
