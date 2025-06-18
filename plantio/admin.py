from django.contrib import admin
from .models import Propriedade, Cultura, Plantio, Colheita, Insumo, Funcionario, UsoInsumo

admin.site.register(Propriedade)
admin.site.register(Cultura)
admin.site.register(Plantio)
admin.site.register(Colheita)
admin.site.register(Insumo)
admin.site.register(Funcionario)
admin.site.register(UsoInsumo)
