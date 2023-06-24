from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    descricao1 = models.CharField(max_length=200)
    descricao2 = models.TextField()
    slug = models.SlugField()
    data_publicacao = models.DateField()
    total_de_paginas = models.CharField(max_length=13)
    capa = models.ImageField(upload_to='livros/capas/%Y/%m/%d/')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )