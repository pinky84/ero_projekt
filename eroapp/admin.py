from django.contrib import admin

from .models import Lokacija, Zgrada, Prostorija, Korisnik, Uredaj, Kvar

# Register your models here.

admin.site.register(Lokacija)
admin.site.register(Zgrada)
admin.site.register(Prostorija)
admin.site.register(Korisnik)
admin.site.register(Uredaj)
admin.site.register(Kvar)