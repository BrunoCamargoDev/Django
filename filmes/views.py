# from django.views import View
# from django.http import HttpResponse
# from pyexpat import model
# from re import search, template
# from typing import OrderedDict
# from unicodedata import name
# from django.shortcuts import render,redirect
from filmes.models import filme
from filmes.forms import FilmesModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class FilmesListView(ListView):
  model = filme
  template_name = 'filmes.html'
  context_object_name = 'filmes'

  def get_queryset(self):
    filmes = super().get_queryset().order_by('titulo')
    titulo = self.request.GET.get('titulo')
    ator = self.request.GET.get('ator')
    if titulo:
      filmes = filmes.filter(titulo__contains=titulo)
    if ator:
      filmes = filmes.filter(atores__nome__icontains=ator)
    return filmes


class FilmeDetailView(DetailView):
  model = filme
  template_name = 'filme_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
# realiza uma verficação de requisição
class NovoFilmeCreateView(CreateView):
  model = FilmesListView
  form_class = FilmesModelForm
  template_name = 'novo_filme.html'
  success_url = '/filmes/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeUpdateView(UpdateView):
  model = filme
  form_class = FilmesModelForm
  template_name = 'filme_update.html'

  def get_success_url(self):
      return reverse_lazy('filme_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeDeleteView(DeleteView):
  model = filme
  template_name = 'filme_delete.html'
  success_url = '/filmes/'

#class FilmesView(View):
#   def get(self, request):
#     filmes = filme.objects.all().order_by('titulo')
#     search = request.GET.get('search')
#     if search:
#       filmes = filme.objects.filter(titulo__contains=search)

#     return render(request, 'filmes.html', {'filmes': filmes})

# class NovoFilmesView(View):
#   def post(self, request):
#     novo_filme_form = FilmesModelForm(request.POST, request.FILES)
#     if novo_filme_form.is_valid():
#       novo_filme_form.save()
#       return redirect('filmes_list')
#     return render(request, 'novo_filme.html', {'novo_filme_form': novo_filme_form})



# def novo_filme_view(request):
#   if request.method == 'POST':
#     novo_filme_form = FilmesModelForm(request.POST, request.FILES)
#     if novo_filme_form.is_valid():
#        novo_filme_form.save()
#        return redirect('filmes_list')
#   else:
#       novo_filme_form = FilmesModelForm()
#   return render(request, 'novo_filme.html', {'novo_filme_form': novo_filme_form})
 
 
 
 
 
 
 

# # # Create your views here.
# def filmes_list(request):
#     filmes = filme.objects.all().order_by('titulo')
#     search = request.GET.get('search')
#     # filmes = filme.objects.filter(titulo='As Branquelas')
#     # filmes = filme.objects.filter (ano=2023)#                            Vê qual usar ai
#     if search:
#       filmes = filme.objects.filter(titulo__contains=search)

#     return render(request, 'filmes.html', {'filmes': filmes})

