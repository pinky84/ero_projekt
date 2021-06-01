from django.db import models

# Create your models here.
class Lokacija(models.Model):
    sifra_lokacije  = models.CharField(max_length=9, unique=True, blank=False)
    mjesto          = models.CharField(max_length=48, blank=False)

    def __str__(self):
        #return (self.sifra_lokacije)
        return '{} {}'.format(self.sifra_lokacije, self.mjesto)

    class Meta:
        verbose_name_plural = 'Lokacije'

#------------------------------------------------------------------------------------------------------------------

class Zgrada(models.Model):
    sifra_zgrade    = models.CharField(max_length=9, unique=True, blank=False)
    adresa          = models.CharField(max_length=50)
    subnet          = models.CharField(max_length=20)
    id_lokacija     = models.ForeignKey(Lokacija, on_delete=models.CASCADE)

    def __str__(self):
        return (self.sifra_zgrade)
        #return '%s %s %s' % (self.sifra_zgrade, self.adresa, self.subnet)

    class Meta:
        verbose_name_plural = 'Zgrade'

#-----------------------------------------------------------------------------------------------------------------

class Prostorija(models.Model):
    sifra_prostorije    = models.CharField(max_length=9, unique=True, blank=False)
    kat             = models.CharField(max_length=15, blank=False)
    broj_prostorije = models.CharField(max_length=15)
    id_zgrada       = models.ForeignKey(Zgrada, on_delete=models.CASCADE)

    def __str__(self):
        return self.sifra_prostorije

    class Meta:
        verbose_name_plural = 'Prostorije'

#----------------------------------------------------------------------------------------------------------------

class Korisnik(models.Model):
    id_korisnika    = models.CharField(max_length=11, unique=True, blank=False)
    ime             = models.CharField(max_length=30, blank=False)
    prezime         = models.CharField(max_length=50, blank=False)

    def __str__(self):
        #return self.id_korisnika
        return '{} {}'.format(self.prezime, self.ime)

    class Meta:
        verbose_name_plural = 'Korisnici'

#---------------------------------------------------------------------------------------------------------------

class Uredaj(models.Model):
    barcode         = models.CharField(max_length=15, unique=True, blank=False)
    serijski_broj   = models.CharField(max_length=20, unique=True, blank=False)
    IZBOR_UREDAJA   = (
        ('PC', 'PC'),
        ('Monitor', 'Monitor'),
        ('Printer', 'Printer'),
        ('Laptop', 'Laptop'),
        ('Telefon', 'Telefon'),
        ('Server', 'Server'),
        ('Storage', 'Storage'),
        ('Mreža', 'Mreža'),
    )
    vrsta_uredaja   = models.CharField(max_length=50, choices=IZBOR_UREDAJA, blank=False)
    IZBOR_PROIZVODACA   = (
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('Lenovo', 'Lenovo'),
        ('Lexmark', 'Lexmark'),
        ('Cisco', 'Cisco'),
    )
    proizvodac      = models.CharField(max_length=30, choices=IZBOR_PROIZVODACA, blank=False)
    model           = models.CharField(max_length=50, blank=True)
    mac_adresa      = models.CharField(max_length=30, blank=True)
    opis            = models.TextField(max_length=1000, blank=True)
    napomena        = models.TextField(max_length=1000, blank=True)
    datum_nabave    = models.DateField(blank=True)
    datum_isteka_garancije  = models.DateField(blank=True)
    id_prostorija   = models.ForeignKey(Prostorija, on_delete=models.CASCADE)
    korisnik_id     = models.ForeignKey(Korisnik, on_delete=models.CASCADE)

    def __str__(self):
        return self.barcode

    class Meta:
        verbose_name_plural = 'Uredaji'

#-----------------------------------------------------------------------------------------------------------------------
 
class Kvar(models.Model):
    id_kvara    = models.CharField(max_length=20, unique=True, blank=False)
    opis_kvara  = models.TextField(max_length=100)
    IZBOR_STATUSA   = (
            ('U tijeku', 'U tijeku'),
            ('Rijesen', 'Rijesen'),
            ('Nerijesivo', 'Nerijesivo'),
        )
    status      = models.CharField(max_length=50, choices=IZBOR_STATUSA)
    barcode_uredaja = models.ForeignKey(Uredaj, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_kvara

    class Meta:
        verbose_name_plural = 'Kvarovi'

#----------------------------------------------------------------------------------------------------------------------------------