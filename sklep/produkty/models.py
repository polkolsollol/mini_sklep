from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nazwa} - {self.cena} PLN'
