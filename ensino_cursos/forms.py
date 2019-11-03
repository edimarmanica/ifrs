import json
from django import forms
from ensino_cursos.models import Curso, ComponenteCurricular

class ComponenteCurricularForm(forms.ModelForm):

#     dcursos = {}
#     list_turmas = []
#     for turma in Turma.objects.all():
#         if turma.curso.pk in dcursos:
#             dturmas[turma.curso.pk].append(turma.pk)
#         else:
#             dturmas[turma.curso.pk] = [turma.pk]
#         list_turmas.append((turma.pk, turma.pk))
#    
     curso_select = forms.ChoiceField(choices=([(curso.pk, curso.denominacao) for curso in Curso.objects.all()])) #(value, text) do select
#     turma_select = forms.ChoiceField(choices=(list_turmas))
# 
#     cursos = json.dumps(cursos)
#     turmas = json.dumps(dturmas)
# 
     class Meta:
         model = ComponenteCurricular
         fields = '__all__' #todos os campos do model + form
     
     class Media:
        js = ('js/componentecurricular.js',)