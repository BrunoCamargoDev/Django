from re import search
from django.contrib import admin
from .models import Ator, filme
from .models import genero
from .models import diretor

# Registre seus modelos aqui

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'duracao', 'ano', 'diretor')
    search_fields = ('titulo', 'genero', 'diretor')
    filter_horizontal = ('atores',)
admin.site.register(filme, FilmeAdmin)

class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento')
    search_fields = ('nome',)
admin.site.register(Ator, AtorAdmin)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
admin.site.register(genero, GeneroAdmin)

class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
admin.site.register(diretor, DiretorAdmin)