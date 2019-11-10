from django.db import models

#minhas classes
from gp.models import Docente
from ensino_cursos.models import ComponenteCurricular

CHOICES_SITUACAO = ( #não alterar números
  (0, "Solicitado"),
  (1, "Aceito pelo Substituto"),
  (2, "Rejeitado pelo Substituto"),
  (3, "Aprovado pela coordenação de ensino"),
  (4, "Rejeitado pela coordenação de ensino"),
  (5, "Cancelado")
)

# Create your models here.
class Periodo(models.Model):
    periodo  = models.CharField(max_length=15, verbose_name="Período - Turno")
    horario_inicial = models.TimeField(verbose_name="Horário Inicial")
    horario_final = models.TimeField(verbose_name="Horário Final")
     
    def __str__(self):
       return self.periodo
    
    class Meta:
        ordering = ["horario_inicial"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Período" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Períodos" #nome dos objetos dessa tabela no plural
                
     
class AplicacaoAtividade(models.Model):
    solicitante = models.ForeignKey(Docente, on_delete=models.PROTECT, verbose_name="Professor(a) solicitante", related_name="solicitante")
    componente_curricular = models.ForeignKey(ComponenteCurricular, on_delete=models.PROTECT, verbose_name="Componente Curricular")
    data_substituicao = models.DateField(verbose_name="Data da substituição")
    data_solicitacao = models.DateField(verbose_name="Data da solicitação")
    justificativa = models.TextField()
    periodos = models.ManyToManyField(Periodo, verbose_name="Períodos")
    substituto = models.ForeignKey(Docente, on_delete=models.PROTECT, verbose_name="Professor(a) substituto", related_name="substituto")            
    situacao = models.IntegerField(choices=CHOICES_SITUACAO, verbose_name="Situação", default=0)
    data_substituto = models.DateField(verbose_name="Data da parecer substituto", blank=True, null=True)
    justificativa_substituto = models.TextField(blank=True, null=True, verbose_name="Justificativa do Substituto")
    data_ensino = models.DateField(verbose_name="Data da parecer Ensino", blank=True, null=True)
    justificativa_coord_ensino = models.TextField(blank=True, null=True, verbose_name="Justificativa do(a) Coord. de Ensino")
    
class MinhasSolicitacoesAplicacao(AplicacaoAtividade):
    
    def __str__(self):
       return self.componente_curricular.denominacao + " - " + self.data_substituicao.strftime("%d/%m/%Y")
    
    class Meta:
        proxy = True
        ordering = ["-data_substituicao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Solicitar Aplicação de Atividade" #nome do objetos dessa tabela
        verbose_name_plural="Solicitar de Aplicação de Atividade" #nome dos objetos dessa tabela no plural

class AceitarSolicitacaoAplicacao(AplicacaoAtividade):
    
    def __str__(self):
       return self.componente_curricular.denominacao + " - " + self.data_substituicao.strftime("%d/%m/%Y")
    
    class Meta:
        proxy = True
        ordering = ["-data_substituicao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Aceitar/Rejeitar Aplicação de Atividade" #nome do objetos dessa tabela
        verbose_name_plural="Aceitar/Rejeitar Aplicação de Atividade" #nome dos objetos dessa tabela no plural

        
#cancelar troca: lista a nXn aí pode marcar vários
#aprovar troca: lista a nXn aí pode marcar vários
#rejeitar troca: lista a nXn aí pode marcar vários. Aí pede a justificativa
