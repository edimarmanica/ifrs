from django.contrib import admin
from datetime import datetime
from django.db import transaction
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q

#minhas classes
from ensino_substituicoes.models import Periodo, AplicacaoAtividade, MinhasSolicitacoesAplicacao, AceitarSolicitacaoAplicacao, DeferirSolicitacaoAplicacao
from gp.models import Docente

class MinhasSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    actions = ['cancelar'] 
    list_display_links = None #desabilita o link para a edição na listagem
    fields = ('componente_curricular', 'data_substituicao', 'substituto', 'justificativa')  # definindo o que será exibido na manutenção
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


#o professor aceita/rejeita aplicar atividade para o solicitante
class AceitarSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    actions = ['aceitar', 'rejeitar'] 
    list_display_links = None #desabilita o link para a edição na listagem
    fields = ('componente_curricular', 'data_substituicao')  # definindo o que será exibido na manutenção
    list_display = ('componente_curricular', 'data_substituicao', 'solicitante', 'situacao', 'justificativa')  # definindo o que será exibido na listagem
    list_filter = ('solicitante', 'situacao')  #definindo os filtros
    search_fields = ['componente_curricular' ]
    
    def get_queryset(self, request):
        return self.model.objects.filter(substituto = request.user) #exibe apenas as solicitações onde o usuário será o substituto
    
    def save_model(self, request, obj, form, change):
        pass #não pode adicionar nem alterar 
            
    def aceitar(self, request, queryset):
        nr_aceites = 0
        try:
            with transaction.atomic():
                for obj in queryset:
                    if obj.situacao == 0 or obj.situacao == 2: #solicitada ou rejeitada
                        obj.situacao = 1 #Aceito
                        obj.save()
                        nr_aceites +=1
                    else:
                        raise IntegrityError
            self.message_user(request, "Aceites efetuados: {}".format(nr_aceites))
        except IntegrityError:
            self.message_user(request, "Apenas solicitações com situação='Solicitada' ou situação='Rejeitada' podem ser aceitas. Informe o solicitante para cancelar esta solicitação e gerar uma nova.", level=messages.ERROR)
    aceitar.short_description = "Aceitar as Solicitações de Aplicação de Atividade selecionadas."
    
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
            self.message_user(request, "Apenas solicitações com situação='Solicitado' podem ser rejeitadas. Informe o solicitante para cancelar esta solicitação.", level=messages.ERROR)
    rejeitar.short_description = "Rejeitar as Solicitações de Aplicação de Atividade selecionadas."

    #removendo a opção de excluir
    def get_actions(self, request):
        actions = super().get_actions(request)    
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


#o coordenador de ensino deferi/indefere a aplicação de atividade
class DeferirSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    actions = ['deferir', 'indeferir'] 
    list_display_links = None #desabilita o link para a edição na listagem
    fields = ('componente_curricular', 'data_substituicao')  # definindo o que será exibido na manutenção
    list_display = ('componente_curricular', 'data_substituicao', 'solicitante', 'substituto', 'situacao', 'justificativa')  # definindo o que será exibido na listagem
    list_filter = ('solicitante', 'substituto', 'situacao')  #definindo os filtros
    search_fields = ['componente_curricular' ]
    
    def get_queryset(self, request):
        return self.model.objects.filter() 
    
    def save_model(self, request, obj, form, change):
        pass #não pode adicionar nem alterar 
            
    def deferir(self, request, queryset):
        nr_deferimentos = 0
        try:
            with transaction.atomic():
                for obj in queryset:
                    if obj.situacao == 1: #
                        obj.situacao = 3 #Deferida
                        obj.save()
                        nr_deferimentos +=1
                    else:
                        raise IntegrityError
            self.message_user(request, "Deferimentos efetuados: {}".format(nr_deferimentos))
        except IntegrityError:
            self.message_user(request, "Apenas solicitações com situação='Aceita' ou situação='Indeferida' podem ser deferidas.", level=messages.ERROR)
    deferir.short_description = "Deferir as Solicitações de Aplicação de Atividade selecionadas."
    
    def indeferir(self, request, queryset):
        self.message_user(request, "Não implementada.", level=messages.ERROR)
    indeferir.short_description = "Indeferir as Solicitações de Aplicação de Atividade selecionadas."

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
admin.site.register(DeferirSolicitacaoAplicacao, DeferirSolicitacaoAplicacaoAdmin)