from django.contrib import admin

#minhas classes
from ensino_substituicoes.models import Periodo, AplicacaoAtividade

# Register your models here.
admin.site.register(Periodo)
admin.site.register(AplicacaoAtividade)