from django.contrib import admin

# Register your models here.
from gp.models import Titulacao, RegimeTrabalho, SituacaoFuncional, AreaConcurso, Servidor

class AreaConcursoAdmin(admin.ModelAdmin):
    list_display = ('area', 'area_pai', 'nivel')  # definindo o que será exibido na listagem
    list_filter = ('area_pai', 'nivel')  #definindo os filtros
    search_fields = ['area', 'area_pai' ]

class ServidorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'groups', 'cpf', 'siape', 'titulacao', 'regime_trabalho', 'situacao_funcional', 'residencia', 'inicio', 'fim') #define os campos e sua ordem no admin
    list_display = ('first_name', 'last_name', 'username', 'cpf', 'siape', 'email', )  # definindo o que será exibido na listagem
    list_filter = ('is_active', )  #definindo os filtros
    search_fields = ['first_name', 'last_name', ]
    
    # cpf, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, siape, user_permissions, user_ptr, user_ptr_id, username
    

admin.site.register(Titulacao)
admin.site.register(RegimeTrabalho)
admin.site.register(SituacaoFuncional)
admin.site.register(AreaConcurso, AreaConcursoAdmin)
admin.site.register(Servidor, ServidorAdmin)

