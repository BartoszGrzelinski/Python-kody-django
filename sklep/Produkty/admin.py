from django.contrib import admin
from .models import Kategoria, Produkty, Producent, Tagi
# Register your models here.
admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Tagi)