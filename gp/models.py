from django.db import models
from django.contrib.auth.models import User

#minhas classes e funções
from ifrs.validator import validate_CPF

CHOICES_RESIDENCIA = (
  (0, "Já morava em Ibirubá"),
  (1, "Mudou-se para Ibirubá em função do concurso"),
  (2, "Não mora em Ibirubá")
)

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
        
class Servidor(User):
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF])
    siape = models.CharField(unique=True, max_length=10)
    titulacao = models.ForeignKey(Titulacao, on_delete=models.PROTECT, verbose_name="Titulação")
    regime_trabalho = models.ForeignKey(RegimeTrabalho, on_delete=models.PROTECT, verbose_name="Regime de Trabalho")
    situacao_funcional = models.ForeignKey(SituacaoFuncional, on_delete=models.PROTECT, verbose_name="Situação Funcional")
    residencia = models.IntegerField(choices=CHOICES_RESIDENCIA, verbose_name="Residência")
    inicio = models.DateField(verbose_name="Início no Campus", help_text="Data em que o servidor entrou em efetivo exercício no Campus.")
    fim = models.DateField(verbose_name="Saída do Campus", blank=True, null=True, help_text="Último dia que o servidor esteve em efetivo exercício no Campus.")

    
    #tornando alguns campos da superclasse obrigatórios
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('last_name').blank = False
    User._meta.get_field('email').blank = False
    
    #adicionando tip para alguns campos da superclasse
    User._meta.get_field('first_name').help_text = "Por exemplo, se seu nome é 'João Carlos Martins da Silva', preencha neste campo 'João'"
    User._meta.get_field('last_name').help_text = "Por exemplo, se seu nome é 'João Carlos Martins da Silva', preencha neste campo 'Carlos Martins da Silva'"
    
    def save(self, force_insert=False, force_update=False):
        if self._state.adding:
            self.username = self.cpf # username é o CPF
            self.set_password(self.siape) # a senha inicial é o SIAPE
        super(Servidor, self).save(force_insert, force_update)
    
    def __str__(self):
       return self.first_name + " " + self.last_name
   
    class Meta:
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name_plural="Servidores" #nome dos objetos dessa tabela no plural
 