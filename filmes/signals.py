from django.db.models.signals import pre_save
from django.dispatch import receiver
from filmes.models import filme
from API_openai.client import get_filme_sinopse

@receiver(pre_save, sender=filme)
def filme_pre_save(sender, instance, **kwargs):
    if not instance.sinopse:
        IA_sinopse = get_filme_sinopse(
            titulo = instance.titulo,
            ano=instance.ano,
            diretor=instance.diretor,
            atores=instance.atores
        )
        instance.sinopse = IA_sinopse