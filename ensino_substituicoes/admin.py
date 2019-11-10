from django.contrib import admin
from datetime import datetime
from django.db import transaction
from django.contrib import messages
from django.db import IntegrityError

#minhas classes
from ensino_substituicoes.models import Periodo, AplicacaoAtividade, MinhasSolicitacoesAplicacao, AceitarSolicitacaoAplicacao
from gp.models import Docente

class MinhasSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    actions = ['cancelar'] 
    list_display_links = None #desabilita o link para a edição na listagem
    fields = ('componente_curricular', 'data_substituicao', 'substituto')  # definindo o que será exibido na manutenção
    list_display = ('componente_curricular', 'data_substituicao', 'substituto', 'situacao')  # definindo o que será exibido na listagem
    list_filter = ('substituto', 'situacao')  #definindo os filtros
    search_fields = ['componente_curricular' ]
    
    def get_queryset(self, request):
        return self.model.objects.filter(solicitante = request.user)
    
    def save_model(self, request, obj, form, change):
        if not(change): # se está adicionando
            obj.solicitante = Docente.objects.get(pk=request.user.pk)
            obj.data_solicitacao = datetime.today()
            obj.situacao = 0 #Solicitado
            super(MinhasSolicitacaoAplicacaoAdmin, self).save_model(request, obj, form, change)
        else:
            pass #não altera pq não é permitido alterar 
            
    def cancelar(self, request, queryset):
        nr_cancelamentos = 0
        for obj in queryset:
            if obj.situacao != 5:
                obj.situacao = 5 #Cancelado
                obj.save()
                nr_cancelamentos +=1
        self.message_user(request, "Cancelamentos realizados: {}".format(nr_cancelamentos))
    cancelar.short_description = "Cancelar Solicitações de Aplicação de Atividade selecionadas."
    
    #removendo a opção de excluir
    def get_actions(self, request):
        actions = super().get_actions(request)    
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AceitarSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    actions = ['aceitar', 'rejeitar'] 
    list_display_links = None #desabilita o link para a edição na listagem
    fields = ('componente_curricular', 'data_substituicao', 'solicitante')  # definindo o que será exibido na manutenção
    list_display = ('componente_curricular', 'data_substituicao', 'solicitante', 'situacao')  # definindo o que será exibido na listagem
    list_filter = ('solicitante', 'situacao')  #definindo os filtros
    search_fields = ['componente_curricular' ]
    
    def get_queryset(self, request):
        return self.model.objects.filter(substituto = request.user)
    
    def save_model(self, request, obj, form, change):
        pass #não pode adicionar nem alterar 
            
    def aceitar(self, request, queryset):
        nr_aceites = 0
        try:
            with transaction.atomic():
                for obj in queryset:
                    if obj.situacao == 0: #solicitado
                        obj.situacao = 1 #Aceito
                        obj.save()
                        nr_aceites +=1
                    else:
                        raise IntegrityError
            self.message_user(request, "Aceites efetuados: {}".format(nr_aceites))
        except IntegrityError:
            self.message_user(request, "Algumas solicitações não podem ser aceitas. Nenhum item foi modificado.", level=messages.ERROR)
    aceitar.short_description = "Aceitar Solicitações de Aplicação de Atividade selecionadas."
    
    def rejeitar(self, request, queryset):
        nr_rejeicoes = 0
        try:
            with transaction.atomic():
                for obj in queryset:
                    if obj.situacao == 0: #solicitado
                        obj.situacao = 2 #Rejeição
                        obj.save()
                        nr_rejeicoes +=1
                    else:
                        raise IntegrityError
            self.message_user(request, "Rejeições efetuadas: {}".format(nr_rejeicoes))
        except IntegrityError:
            self.message_user(request, "Algumas solicitações não podem ser rejeitadas. Nenhum item foi modificado.", level=messages.ERROR)
    rejeitar.short_description = "Rejeitar Solicitações de Aplicação de Atividade selecionadas."

    #removendo a opção de excluir
    def get_actions(self, request):
        actions = super().get_actions(request)    
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
# Register your models here.
admin.site.register(Periodo)
admin.site.register(AplicacaoAtividade)
admin.site.register(MinhasSolicitacoesAplicacao, MinhasSolicitacaoAplicacaoAdmin)
admin.site.register(AceitarSolicitacaoAplicacao, AceitarSolicitacaoAplicacaoAdmin)