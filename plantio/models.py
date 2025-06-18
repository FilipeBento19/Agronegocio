from django.db import models


class Propriedade(models.Model):
    nomePropriedade = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=150)

    def __str__(self):
        return self.nomePropriedade


class Cultura(models.Model):
    nomeCultura = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeCultura


class Plantio(models.Model):
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    areaPlantada = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Plantio de {self.cultura} em {self.propriedade}"


class Colheita(models.Model):
    plantio = models.ForeignKey(Plantio, on_delete=models.CASCADE)
    dataColheita = models.DateField()
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Colheita em {self.dataColheita} - {self.quantidade}"
