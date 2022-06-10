from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Producent(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"
class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
class Tagi(models.Model):
    def __str__(self):
        return self.name
    name    = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name        = "Tag"
        verbose_name_plural = "Tagi"


class Produkty(models.Model):
    def __str__(self):
        return self.nazwa
    Kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent,on_delete=models.CASCADE,null=True)
# w razie usuniecia usuwa wszystkie produkty jakie posiada , taka jakby blokada
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=99999, decimal_places=2)
    tagi = models.ManyToManyField(Tagi,blank=True)
   
    
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    