from django.db import models


class Plantio(models.Model):
    propriedade = models.CharField(max_length=50)
    cultura = models.CharField(max_length=50)
    areaPlantada = models.CharField(max_length=100)
    dataPlantio = models.DateField()
    observacoes = models.CharField(max_length=50)

    def __str__(self):
        return self.propriedade
    

class Cultura(models.Model):
    nomeCultura = models.CharField(max_length=50)
    tipoCultura = models.CharField(max_length=50)
    epocaCultura = models.CharField(max_length=100)


