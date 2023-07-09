from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return self.name


class Livro(models.Model):
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
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.titulo)}'
            self.slug = slug

        return super().save(*args, **kwargs)