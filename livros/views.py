from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ultils.livros.fabrica_de_livros import make_livro
from livros.models import Livro
from django.shortcuts import get_list_or_404, get_object_or_404, render

def home(request):
    livros = Livro.objects.filter(
        publicado=True
    ).order_by('-id')

    return render(request, "livros/paginas/home.html", context={
        "livros": livros,
    })


def category(request, category_id):
    livros = Livro.objects.filter(
        category__id=category_id,
        publicado=True
    ).order_by('-id')
    return render(request, 'livros/paginas/categoria.html', context={
        'livros': livros,
        'titulo': f'{livros.first().category.name} - Category | '
    })


def livro(request, id):


    livro = get_object_or_404(Livro, pk=id, publicado=True,)

    return render(request, 'livros/paginas/livro-view.html', context={
        'livro': livro,
        'detalhe_da_pagina': True,
    })
