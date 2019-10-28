from django.contrib import admin

# Register your models here.
from gp.models import Titulacao, RegimeTrabalho, SituacaoFuncional, AreaConcurso

class AreaConcursoAdmin(admin.ModelAdmin):
    list_display = ('area', 'area_pai', 'nivel')  # definindo o que será exibido na listagem
    list_filter = ('area_pai', 'nivel')  #definindo os filtros
    search_fields = ['area', 'area_pai' ]


admin.site.register(Titulacao)
admin.site.register(RegimeTrabalho)
admin.site.register(SituacaoFuncional)
admin.site.register(AreaConcurso, AreaConcursoAdmin)

