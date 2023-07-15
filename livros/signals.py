import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from livros.models import Livro


def delete_capa(instance):
    try:
        os.remove(instance.capa.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Livro)
def livro_capa_delete(sender, instance, *args, **kwargs):
    old_instance = Livro.objects.get(pk=instance.pk)
    delete_capa(old_instance)
    
@receiver(pre_save, sender=Livro)
def livro_capa_update(sender, instance, *args, **kwargs):
    old_instance = Livro.objects.get(pk=instance.pk)
    is_new_capa = old_instance.capa != instance.capa

    if is_new_capa:
        delete_capa(old_instance)