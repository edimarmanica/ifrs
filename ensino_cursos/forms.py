import json
from django import forms
from ensino_cursos.models import Curso, ComponenteCurricular, Turma

class ComponenteCurricularForm(forms.ModelForm):
    

    dic_turmas = {}  #dicionário de turmas -- Para achar mais rápdio uma vez que a chave será a pk do curso da turma
    turmas = Turma.objects.all()
    for turma in turmas:
         if turma.curso.pk in dic_turmas:
            dic_turmas[turma.curso.pk].append(turma.pk) #depois terei que ver como add pk e denominacao
         else:
            dic_turmas[turma.curso.pk] = [turma.pk]
#    
    curso_select = forms.ChoiceField(choices=([(curso.pk, curso.denominacao) for curso in Curso.objects.all()])) #(value, text) do select
# 
    cursos = json.dumps([str(curso) for curso in Curso.objects.all()])
    turmas = json.dumps(dic_turmas)
# 
    class Meta:
        model = ComponenteCurricular
        fields = '__all__' #todos os campos do model + form
     
    class Media:
        js = ('js/componentecurricular.js',)