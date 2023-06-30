from django.shortcuts import render
from livros.models import Livro
from django.shortcuts import get_object_or_404, render
from django.http.response import Http404
from django.db.models import Q
from ultils.livros.paginaçao import paginaçao_das_page
import os



QT_LIVROS_NA_PAG = int(os.environ.get("QT_LIVROS_NA_PAG", 2))


def home(request):
    livros = Livro.objects.filter(
        publicado=True
    ).order_by('-id')


    
    pagina_obj, pagination_range = paginaçao_das_page(request,livros, QT_LIVROS_NA_PAG)

    return render(request, "livros/paginas/home.html", context={
        "livros": pagina_obj,
        "pagination_range":pagination_range,
    })


def category(request, category_id):
    livros = Livro.objects.filter(
        category__id=category_id,
        publicado=True
    ).order_by('-id')

    pagina_obj, pagination_range = paginaçao_das_page(request,livros, QT_LIVROS_NA_PAG)

    return render(request, 'livros/paginas/categoria.html', context={
        "livros": pagina_obj,
        "pagination_range":pagination_range,
        'titulo': f'{livros[0].category.name} - Category | '
    })


def livro(request, id):


    livro = get_object_or_404(Livro, pk=id, publicado=True,)

    return render(request, 'livros/paginas/livro-view.html', context={
        'livro': livro,
        'detalhe_da_pagina': True,
    })
def search(request):
    
    search_term = request.GET.get('q', '').strip()


    if not search_term:
        raise Http404()

    livros = Livro.objects.filter(
        Q(
            Q(titulo__icontains=search_term) | 
            Q(descricao1__icontains=search_term),
        ),
        publicado=True
    ).order_by('-id')
    
    pagina_obj, pagination_range = paginaçao_das_page(request,livros, QT_LIVROS_NA_PAG)



    return render(request, 'livros/paginas/search.html', context={
        'page_titulo': f"Pesquisa por {search_term}",
        'search_term': search_term,
        "livros": pagina_obj,
        "pagination_range":pagination_range,
        "adicional_url": f"&q={search_term}",
    })