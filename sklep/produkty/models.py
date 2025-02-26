from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazwa
from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100, verbose_name='Nazwa produktu')
    cena = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena produktu')

    def __str__(self):
        return f'{self.nazwa} - {self.cena}'
