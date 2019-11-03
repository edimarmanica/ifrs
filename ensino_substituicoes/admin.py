from django.contrib import admin

#minhas classes
from ensino_substituicoes.models import Periodo, AplicacaoAtividade, MinhasSolicitacoesAplicacao

class MinhasSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    list_display = ('componente_curricular', 'data_substituicao', 'substituto', 'situacao')  # definindo o que será exibido na listagem
    list_filter = ('substituto', )  #definindo os filtros
    search_fields = ['componente_curricular' ]
    


# Register your models here.
admin.site.register(Periodo)
admin.site.register(AplicacaoAtividade)
admin.site.register(MinhasSolicitacoesAplicacao, MinhasSolicitacaoAplicacaoAdmin)