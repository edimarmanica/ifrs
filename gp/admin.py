from django.contrib import admin

# Register your models here.
from gp.models import Titulacao, RegimeTrabalho, SituacaoFuncional, AreaConcurso, Docente

class AreaConcursoAdmin(admin.ModelAdmin):
    list_display = ('area', 'area_pai', 'nivel')  # definindo o que será exibido na listagem
    list_filter = ('area_pai', 'nivel')  #definindo os filtros
    search_fields = ['area', 'area_pai' ]

class DocenteAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'groups', 'cpf', 'siape', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'residencia', 'formacao_pedagogica', 'area_concurso', 'inicio', 'fim', 'observacoes') #define os campos e sua ordem no admin
    list_display = ('cpf', 'first_name', 'last_name', 'siape', 'email', 'regime_trabalho', 'situacao_funcional', 'formacao_pedagogica')  # definindo o que será exibido na listagem
    list_filter = ('is_active', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'formacao_pedagogica', )  #definindo os filtros
    search_fields = ['first_name', 'last_name', ]
    

admin.site.register(Titulacao)
admin.site.register(RegimeTrabalho)
admin.site.register(SituacaoFuncional)
admin.site.register(AreaConcurso, AreaConcursoAdmin)
admin.site.register(Docente, DocenteAdmin)

