from django.contrib import admin

# Register your models here.
from servidores.models import Servidor

class ServidorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'cpf', 'siape') #define os campos e sua ordem no admin
    list_display = ('first_name', 'last_name', 'username', 'cpf', 'siape', 'email', )  # definindo o que será exibido na listagem
    list_filter = ('is_active', )  #definindo os filtros
    search_fields = ['first_name', 'last_name', ]
    
    # cpf, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, siape, user_permissions, user_ptr, user_ptr_id, username

admin.site.register(Servidor, ServidorAdmin)