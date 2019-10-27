from django.db import models
from django.contrib.auth.models import User

#minhas classes e funções
from ifrs.validator import validate_CPF

# Create your models here.
class Servidor(User):
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF])
    siape = models.CharField(unique=True, max_length=10)
    
    
    #tornando alguns campos da superclasse obrigatórios
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('last_name').blank = False
    User._meta.get_field('email').blank = False
    
    def __str__(self):
       return self.first_name + " " + self.last_name
   
    class Meta:
        ordering = ["first_name", "last_name"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name_plural="Servidores" #nome dos objetos dessa tabela no plural