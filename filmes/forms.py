
from tkinter import Widget
from django import forms
from filmes.models import filme  

# class FilmeForm(forms.Form):
#     titulo = forms.CharField(max_length=100)
#     sinopse = forms.CharField(widget=forms.Textarea)
#     duracao = forms.IntegerField()
#     ano = forms.IntegerField()
#     genero = forms.ModelChoiceField(Genero.objects.all())
#     diretor = forms.CharField(max_length=100)  
#     atores = forms.CharField(max_length=100)
#     poster = forms.ImageField()



#     def save(self):       
#         filme = Filme(
#             titulo=self.cleaned_data['titulo'],
#             sinopse=self.cleaned_data['sinopse'],
#             duracao=self.cleaned_data['duracao'],
#             ano=self.cleaned_data['ano'],
#             genero=self.cleaned_data['genero'],
#             diretor=self.cleaned_data['diretor'],
#             atores=self.cleaned_data['atores'],
#             poster=self.cleaned_data['poster']
#         )
#         filme.save()
#         return filme
    
class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = filme
        fields = '__all__' 
        widgets = {'atores': forms.CheckboxSelectMultiple()}

    def save(self, commit=True):
        instance = super().save(commit=commit)
        return instance

     # As funções que se iniciam com (clean), o Django realiza uma validação
     
     # Limita o digito a 20 
    # def clean_sinopse(self):
    #     sinopse = self.cleaned_data.get('sinopse')
    #     if len(sinopse) < 20:
    #         self.add_error('sinopse', 'A sinopse deve ter pelo menos 20 caracteres.')
    #     return sinopse


    # Verifica o ano 
    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano < 1900 or ano > 2100:
            self.add_error('ano', 'O ano deve estar entre 1900 e 2100.')
        return ano