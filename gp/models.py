from django.db import models
from django.contrib.auth.models import User

#minhas classes e funções
from ifrs.validator import validate_CPF


#############################################################################
##################### SERVIDOR ##############################################
#############################################################################
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

class Remuneracao(models.Model):
    descricao = models.CharField(max_length=5, verbose_name="Descrição")
    
    def __str__(self):
       return self.descricao
       
    class Meta:
        ordering = ["descricao"] 
        verbose_name="Remuneração" 
        verbose_name_plural="Remunerações"             

class Setor(models.Model):
    descricao = models.CharField(max_length=60, verbose_name="Descrição")
    setor_pai = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Setor Pai", related_name="pai")
    remuneracao = models.ForeignKey(Remuneracao, on_delete=models.PROTECT, verbose_name="Remuneração")
    
    def __str__(self):
       return self.descricao
       
    class Meta:
        ordering = ["descricao"]  
        verbose_name_plural="Setores"
       
class Servidor(User):
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF])
    siape = models.CharField(unique=True, max_length=10)
    titulacao = models.ForeignKey(Titulacao, on_delete=models.PROTECT, verbose_name="Titulação")
    regime_trabalho = models.ForeignKey(RegimeTrabalho, on_delete=models.PROTECT, verbose_name="Regime de Trabalho")
    situacao_funcional = models.ForeignKey(SituacaoFuncional, on_delete=models.PROTECT, verbose_name="Situação Funcional")
    residencia = models.IntegerField(choices=CHOICES_RESIDENCIA, verbose_name="Residência")
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name="Setor de Exercício", null=True, blank=True, help_text="Setor onde o servidor está lotado atualmente.")
    inicio = models.DateField(verbose_name="Início do Exercício", help_text="Data em que o servidor entrou em efetivo exercício no Campus.")
    fim = models.DateField(verbose_name="Término do Exercício", blank=True, null=True, help_text="Último dia que o servidor esteve em efetivo exercício no Campus.")
    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)
    
    #tornando alguns campos da superclasse obrigatórios
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('last_name').blank = False
    User._meta.get_field('email').blank = False
    
    #adicionando tip para alguns campos da superclasse
    User._meta.get_field('first_name').help_text = "Por exemplo, se seu nome é 'João Carlos Martins da Silva', preencha neste campo 'João'"
    User._meta.get_field('last_name').help_text = "Por exemplo, se seu nome é 'João Carlos Martins da Silva', preencha neste campo 'Carlos Martins da Silva'"

    #Por padrão um novo usuário é Membro da Equipe    
    User._meta.get_field('is_staff').default = True
    
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
        
        
#############################################################################
###################### DOCENTE ##############################################
#############################################################################
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
        
class Docente(Servidor):
    formacao_pedagogica = models.BooleanField(verbose_name="Formação Pedagógica", help_text="Marque está opção se você possui Licenciatura ou Formação Pedagógica")
    area_concurso = models.ForeignKey(AreaConcurso, on_delete=models.PROTECT, verbose_name="Área Concurso", help_text="Área que consta no edital do concurso")
    
    class Meta:
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name_plural="Docentes" #nome dos objetos dessa tabela no plural


class MeuPerfilDocente(Docente):
    class Meta:
        proxy = True
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Meu Perfil - Docente" #nome do objetos dessa tabela
        verbose_name_plural="Meus Perfis - Docente" #nome dos objetos dessa tabela no plural
                 
#############################################################################
########################## TAE ##############################################
#############################################################################
CHOICES_NIVEIS = (
  (0, "A"),
  (1, "B"),
  (2, "C"),
  (3, "D"),
  (4, "E")
)
    
class Cargo(models.Model):
    descricao = models.CharField(max_length=15, verbose_name="Descrição")
    nivel = models.IntegerField(choices=CHOICES_NIVEIS, verbose_name="Nível")
    
    def __str__(self):
       return self.descricao
       
    class Meta:
        ordering = ["descricao"]  
        
        
class TecnicoAdministrativo(Servidor):
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name ="Técnico Administrativo em Educação"
        verbose_name_plural="Técnicos Administrativos em Educação" #nome dos objetos dessa tabela no plural
 
 
class MeuPerfilTecnicoAdministrativo(TecnicoAdministrativo):
    class Meta:
        proxy = True
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Meu Perfil - TAE" #nome do objetos dessa tabela
        verbose_name_plural="Meus Perfis - TAE" #nome dos objetos dessa tabela no plural