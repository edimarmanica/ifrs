from django.contrib import admin
from datetime import datetime

#minhas classes
from ensino_substituicoes.models import Periodo, AplicacaoAtividade, MinhasSolicitacoesAplicacao
from gp.models import Docente

class MinhasSolicitacaoAplicacaoAdmin(admin.ModelAdmin):
    #actions = None
    actions = ['cancelar'] #Disabling all actions for a particular ModelAdmin (desabilita exclusão e alteração). Porém, ele continua habilitando o botão salva na edição, só que não salva, precisa complementar com o comando abaixo
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
            
    def cancelar(self, request, queryset):
        nr_cancelamentos = 0
        for obj in queryset:
            if obj.situacao == 0:
                obj.situacao = 5 #Cancelado
                obj.save()
                nr_cancelamentos +=1
        self.message_user(request, "Cancelamentos realizados: {}".format(nr_cancelamentos))
    cancelar.short_description = "Cancelar Solicitações de Aplicação de Atividade selecionadas."
    

# Register your models here.
admin.site.register(Periodo)
admin.site.register(AplicacaoAtividade)
admin.site.register(MinhasSolicitacoesAplicacao, MinhasSolicitacaoAplicacaoAdmin)