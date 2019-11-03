from django.db import models

#minhas classes
from gp.models import Docente

# Create your models here.
class TipoCurso(models.Model):
    descricao = models.CharField(max_length=30, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Tipo de Curso" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Tipos de Cursos" #nome dos objetos dessa tabela no plural


class TipoOferta(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Tipo de Oferta" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Tipos de Ofertas" #nome dos objetos dessa tabela no plural


class Modalidade(models.Model):
    descricao = models.CharField(max_length=20, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        
    
class SituacaoCurso(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Situação do Curso" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Situações dos Cursos" #nome dos objetos dessa tabela no plural

        
class EixoTecnologico(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Eixo Tecnológico" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Eixos Tecnológicos" #nome dos objetos dessa tabela no plural

        
class TurnoFuncionamento(models.Model):
    descricao = models.CharField(max_length=30, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Turno de Funcionamento" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Turnos de Funcionamento" #nome dos objetos dessa tabela no plural

        
class DuracaoPeriodo(models.Model):
    descricao = models.CharField(max_length=10, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Duração do Período" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Durações dos Períodos" #nome dos objetos dessa tabela no plural

        
class PeriodicidadeOferta(models.Model):
    descricao = models.CharField(max_length=10, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Periodicidade de Oferta" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Periodicidades de Oferta" #nome dos objetos dessa tabela no plural
        
class Curso(models.Model):
    denominacao = models.CharField(max_length=80, verbose_name="Denominação")
    tipo_curso = models.ForeignKey(TipoCurso, on_delete=models.PROTECT, verbose_name="Tipo de Curso")
    tipo_oferta = models.ForeignKey(TipoOferta, on_delete=models.PROTECT, verbose_name="Tipo de Oferta")
    modalidade  = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    situacao = models.ForeignKey(SituacaoCurso, on_delete=models.PROTECT, verbose_name="Situação do Curso")
    eixo  = models.ForeignKey(EixoTecnologico, on_delete=models.PROTECT, verbose_name="Eixo Tecnológico")
    habilitacao = models.CharField(max_length=80, verbose_name="Habilitação", help_text = "Digitar a habilitação do egresso. Ex.: Tecnólogo em Processos Gerenciais, Técnico em Plásticos.")
    turno = models.ForeignKey(TurnoFuncionamento, on_delete=models.PROTECT, verbose_name="Turno de Funcionamento")
    duracao_periodo = models.ForeignKey(DuracaoPeriodo, on_delete=models.PROTECT, verbose_name="Duração do Período")
    quantidade_periodos = models.IntegerField(verbose_name="Quantidade de Períodos")
    periodicidade_oferta = models.ForeignKey(PeriodicidadeOferta, on_delete=models.PROTECT, verbose_name="Periodicidade da Oferta")
    nr_vagas = models.IntegerField(verbose_name="Número de Vagas")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária Total", help_text="Digitar a carga horária total do curso, em horas-relógio, excluídos estágios e orientações de TCC.")
    
    def __str__(self):
       return self.denominacao 
   

class Turma(models.Model):
    denominacao = models.CharField(max_length=30, verbose_name="Denominação")
    periodo = models.IntegerField(verbose_name="Período", help_text="Digitar o semestre para cursos semestrais e o ano para cursos anuais.")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
        
    def __str__(self):
       return self.denominacao + " - " + self.curso.denominacao
   
class ComponenteCurricular(models.Model):
     denominacao = models.CharField(max_length=30, verbose_name="Denominação")
     curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
     turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
     
     
     ativo = models.BooleanField(help_text="Desmarque esta opção quando o Componente Curricular não fizer mais parte da turma.", default=True)
     
     def __str__(self):
       return self.denominacao
   
     class Meta:
        ordering = ["denominacao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Componente Curricular" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Componentes Curriculares" #nome dos objetos dessa tabela no plural