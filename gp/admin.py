from django.contrib import admin

# Register your models here.
from gp.models import Titulacao, RegimeTrabalho, SituacaoFuncional, AreaConcurso, Docente, Setor, TecnicoAdministrativo, Remuneracao, Cargo, MeuPerfilTecnicoAdministrativo, MeuPerfilDocente

class AreaConcursoAdmin(admin.ModelAdmin):
    list_display = ('area', 'area_pai', 'nivel')  # definindo o que será exibido na listagem
    list_filter = ('area_pai', 'nivel')  #definindo os filtros
    search_fields = ['area', 'area_pai' ]

class DocenteAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'groups', 'cpf', 'siape', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'residencia', 'formacao_pedagogica', 'area_concurso', 'setor', 'inicio', 'fim', 'observacoes') #define os campos e sua ordem no admin
    list_display = ('cpf', 'first_name', 'last_name', 'siape', 'email', 'regime_trabalho', 'situacao_funcional', 'formacao_pedagogica')  # definindo o que será exibido na listagem
    list_filter = ('is_active', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'formacao_pedagogica', )  #definindo os filtros
    search_fields = ['first_name', 'last_name', ]
    
class MeuPerfilDocenteAdmin(DocenteAdmin):
    fields = ('first_name', 'last_name', 'titulacao', 'situacao_funcional', 'residencia', 'formacao_pedagogica', 'setor') #define os campos e sua ordem no admin
     
    def get_queryset(self, request):
        return self.model.objects.filter(username = request.user.username)
     
    def save_model(self, request, obj, form, change):
        obj.username = request.user.username
        super(MeuPerfilDocenteAdmin, self).save_model(request, obj, form, change)
    
class TaeAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'groups', 'cpf', 'siape', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'residencia', 'cargo', 'setor', 'inicio', 'fim', 'observacoes') #define os campos e sua ordem no admin
    list_display = ('cpf', 'first_name', 'last_name', 'siape', 'email', 'regime_trabalho', 'situacao_funcional', 'cargo', 'nivel')  # definindo o que será exibido na listagem
    list_filter = ('is_active', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'cargo__nivel', )  #definindo os filtros
    search_fields = ['first_name', 'last_name', ]
    
    def nivel(self, obj):
        return obj.cargo.get_nivel_display();
    nivel.short_description = "Nível"
    
class MeuPerfilTaeAdmin(TaeAdmin):
    fields = ('first_name', 'last_name', 'titulacao', 'situacao_funcional', 'residencia', 'setor') #define os campos e sua ordem no admin
    
    def get_queryset(self, request):
        return self.model.objects.filter(username = request.user.username)
    
    def save_model(self, request, obj, form, change):
        obj.username = request.user.username
        super(MeuPerfilTaeAdmin, self).save_model(request, obj, form, change)

admin.site.register(Titulacao)
admin.site.register(RegimeTrabalho)
admin.site.register(SituacaoFuncional)
admin.site.register(Remuneracao)
admin.site.register(Setor)
admin.site.register(AreaConcurso, AreaConcursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(MeuPerfilDocente, MeuPerfilDocenteAdmin)
admin.site.register(Cargo)
admin.site.register(TecnicoAdministrativo, TaeAdmin)
admin.site.register(MeuPerfilTecnicoAdministrativo, MeuPerfilTaeAdmin)

