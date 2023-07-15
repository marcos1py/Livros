from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from django.conf import settings
import os
from django.db.models.functions import Concat

from django.db.models import F, Value


class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return self.name


class LivroManager(models.Manager):
    def get_published(self):
        return self.filter(
            publicado=True
        ).annotate(
            author_full_name=Concat(
                F('author__first_name'), Value(' '),
                F('author__last_name'), Value(' ('),
                F('author__username'), Value(')'),
            )
        ).order_by('-id')

class Livro(models.Model):
    objects = LivroManager()
    titulo = models.CharField(max_length=100)
    descricao1 = models.CharField(max_length=200)
    descricao2 = models.TextField()
    slug = models.SlugField(unique=True)
    data_publicacao = models.DateField(null=True)
    total_de_paginas = models.CharField(max_length=13)

    capa = models.ImageField(
        upload_to='livros/capas/%Y/%m/%d/', blank=True, default='')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('livros:livro', args=(self.id,))

    @staticmethod
    def resize_image(image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.titulo)}'
            self.slug = slug
            
        saved = super().save(*args, **kwargs)
        if self.capa:
            try:
                self.resize_image(self.capa, 840)
            except FileNotFoundError:
                ...

        return saved