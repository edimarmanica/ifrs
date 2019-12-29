from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import AplicacaoAtividade
from .forms import IndeferirAplicacaoAtividadeForm
    
#class IndeferirAplicacaoAtividade(CreateView):
#    model = AplicacaoAtividade
#    form_class = IndeferirAplicacaoAtividadeForm
#    template_name = 'indeferir_aplicacao_atividade.html'
#    success_url = reverse_lazy('AplicacaoAtividade')
    
def indeferir_aplicacao_atividade(request, object):
    #if request.method == 'POST':
    #    form = BandContactForm(request.POST)
    #else:
    #    form = BandContactForm()
    form = IndeferirAplicacaoAtividadeForm()
    return render(request, 'indeferir_aplicacao_atividade.html', {'form': form, 'obj': object})

