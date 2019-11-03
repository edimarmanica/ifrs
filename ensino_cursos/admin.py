from django.contrib import admin

# Register your models here.
from ensino_cursos.models import TipoCurso, TipoOferta, Modalidade, SituacaoCurso, EixoTecnologico, TurnoFuncionamento, DuracaoPeriodo, PeriodicidadeOferta, Curso

admin.site.register(TipoCurso)
admin.site.register(TipoOferta)
admin.site.register(Modalidade)
admin.site.register(SituacaoCurso)
admin.site.register(EixoTecnologico)
admin.site.register(TurnoFuncionamento)
admin.site.register(DuracaoPeriodo)
admin.site.register(PeriodicidadeOferta)
admin.site.register(Curso)