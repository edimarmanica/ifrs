from django.db import models

# Create your models here.
class Titulacao(models.Model):
    descricao = models.CharField(max_length=15, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Titulação" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Titulações" #nome dos objetos dessa tabela no plural
        
class RegimeTrabalho(models.Model):
    descricao = models.CharField(max_length=6, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
       
    class Meta:
        ordering = ["descricao"] 
        verbose_name="Regime de Trabalho" 
        verbose_name_plural="Regimes de Trabalho"
        
class SituacaoFuncional(models.Model):
    descricao = models.CharField(max_length=15, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
       
    class Meta:
        ordering = ["descricao"] 
        verbose_name="Situação Funcional" 
        verbose_name_plural="Situações Funcionais"
        

class AreaConcurso(models.Model):
    area = models.CharField(max_length=50, verbose_name="Área")
    area_pai = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Área Pai", related_name="pai")
    nivel = models.IntegerField(verbose_name="Nível")
    
    def __str__(self):
       return self.area
       
    class Meta:
        ordering = ["area"] 
        verbose_name="Área do Concurso" 
        verbose_name_plural="Áreas do Concurso"
 