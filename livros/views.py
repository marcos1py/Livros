from django.shortcuts import render
from livros.models import Livro
from django.shortcuts import get_object_or_404, render

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
        'titulo': f'{livros[0].category.name} - Category | '
    })


def livro(request, id):


    livro = get_object_or_404(Livro, pk=id, publicado=True,)

    return render(request, 'livros/paginas/livro-view.html', context={
        'livro': livro,
        'detalhe_da_pagina': True,
    })
