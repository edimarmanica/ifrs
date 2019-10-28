from django.db import models

# Create your models here.
class Titulacao(models.Model):
    descricao = models.CharField(max_length=15)
    
    class Meta:
        ordering = ["descricao"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Titulação" #nome dos objetos dessa tabela no singular
        verbose_name_plural="Titulações" #nome dos objetos dessa tabela no plural
        
