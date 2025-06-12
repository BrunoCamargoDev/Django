from django.db import models

class Ator(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class genero(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class diretor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class filme(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(genero, on_delete=models.PROTECT)
    duracao = models.IntegerField()
    ano = models.IntegerField()
    diretor = models.ForeignKey(diretor, on_delete=models.PROTECT)
    sinopse = models.TextField(blank=True, null=True)
    atores = models.ManyToManyField(Ator, related_name='filmes', blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
# Create your models here.
