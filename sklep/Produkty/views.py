from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Produkty, Kategoria
from .forms import Produktform
#def index tutaj mamy wyswietlenie sie produktow w panelu uzytkownika sucha
# # strona all wszystkie get jeden konkretny filter filtrujemy kategorie np
def detail(request, produkt_id):
    produkt = Produkty.objects.get(pk=produkt_id)
    kats = Kategoria.objects.all()

    return render(request, 'produkty/detail_block.html', {'produkt': produkt,
                                                          'kats': kats,})
def produkt_widok(request):
        form = Produktform(request.POST or None)
        if form.is_valid():
                form.save
        context = {
                'form': form
        }
        return render(request, "produkty/produkt_widok.html", context)
def index(request, *args, **kwargs):
        kategorie = Kategoria.objects.all()
        dane = {'kategorie' : kategorie}
        return render(request, 'szablon.html', dane)
def kategoria (request, id):
        kategoria_user = Kategoria.objects.get(pk=id)
        kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
        kategorie = Kategoria.objects.all()
        dane = {'kategoria_user' : kategoria_user,
                'kategoria_produkt' : kategoria_produkt,
                'kategorie' : kategorie}
        return render(request, 'kategoria_produkt.html', dane)
def produkt (request, id):
        produkt_user = Produkty.objects.get(pk=id)
        kategorie = Kategoria.objects.all()
        dane = {'produkt.user' : produkt_user, 'kategorie' : kategorie}
        return render(request, 'produkt.html', dane)