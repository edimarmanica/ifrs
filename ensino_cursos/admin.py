from django.contrib import admin

#minhas classes
from ensino_cursos.models import TipoCurso, TipoOferta, Modalidade, SituacaoCurso, EixoTecnologico, TurnoFuncionamento, DuracaoPeriodo, PeriodicidadeOferta, Curso, Turma, ComponenteCurricular
from ensino_cursos.forms import ComponenteCurricularForm

class TurmaInline(admin.TabularInline):
    model = Turma
    
class CursoAdmin(admin.ModelAdmin):
    list_display = ('denominacao', 'tipo_curso', 'tipo_oferta')  # definindo o que será exibido na listagem
    list_filter = ('tipo_curso', 'tipo_oferta')  #definindo os filtros
    search_fields = ['denominacao' ]
    
    inlines = [
        TurmaInline,
    ]


class ComponenteCurricularInline(admin.TabularInline):
    model = ComponenteCurricular
    

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('denominacao', 'periodo', 'curso')  # definindo o que será exibido na listagem
    list_filter = ('periodo', 'curso')  #definindo os filtros
    search_fields = ['denominacao' ]
    
    inlines = [
        ComponenteCurricularInline,
    ]
    
class ComponenteCurricularAdmin(admin.ModelAdmin):
    list_display = ('denominacao', 'turma', 'ativo')  # definindo o que será exibido na listagem
    list_filter = ('turma', 'ativo')  #definindo os filtros
    search_fields = ['denominacao' ]
    
    form = ComponenteCurricularForm

# Register your models here.
admin.site.register(TipoCurso)
admin.site.register(TipoOferta)
admin.site.register(Modalidade)
admin.site.register(SituacaoCurso)
admin.site.register(EixoTecnologico)
admin.site.register(TurnoFuncionamento)
admin.site.register(DuracaoPeriodo)
admin.site.register(PeriodicidadeOferta)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(ComponenteCurricular, ComponenteCurricularAdmin)