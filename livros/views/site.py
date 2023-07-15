
from livros.models import Livro
from django.shortcuts import get_object_or_404, render
from django.http.response import Http404
from django.db.models import Q
from utils.livros.paginaçao import paginaçao_das_page
import os
from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from django.forms.models import model_to_dict

QT_LIVROS_NA_PAG = int(os.environ.get("QT_LIVROS_NA_PAG", 2))



class LivroListViewBase(ListView):
    model = Livro
    context_object_name = 'livros'
    ordering = ['-id']
    template_name = 'livros/paginas/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            publicado=True,
        )
        qs = qs.select_related('author', 'category', 'author__profile')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = paginaçao_das_page(
            self.request,
            ctx.get('livros'),
            QT_LIVROS_NA_PAG
        )
        ctx.update(
            {'livros': page_obj, 'pagination_range': pagination_range}
        )
        return ctx


class LivroListViewHome(LivroListViewBase):
    template_name = 'livros/paginas/home.html'

class LivroListViewCategory(LivroListViewBase):
    template_name = 'livros/paginas/categoria.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id')
        )
        return qs


class LivroListViewSearch(LivroListViewBase):
    template_name = 'livros/paginas/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q', '')
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term),
            )
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')

        ctx.update({
            'page_titulo': f'Search for "{search_term}" |',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })

        return ctx




def livro(request, id):


    livro = get_object_or_404(Livro, pk=id, publicado=True,)

    return render(request, 'livros/paginas/livro-view.html', context={
        'livro': livro,
        'detalhe_da_pagina': True,
    })
    
class LivroDetail(DetailView):
    model = Livro
    context_object_name = 'livro'
    template_name = 'livros/paginas/livro-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(publicado=True)
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'is_detail_page': True
        })

        return ctx
    
class LivroDetailAPI(DetailView):
    model = Livro
    context_object_name = 'livro'
    template_name = 'livros/paginas/livro-view.html'

    def render_to_response(self, context, **response_kwargs):
        livro = self.get_context_data()['livro']
        livro_dict = model_to_dict(livro)

        livro_dict['criado_em'] = str(livro.criado_em)
        livro_dict['atualizado_em'] = str(livro.atualizado_em)

        if livro_dict.get('capa'):
            livro_dict['capa'] = self.request.build_absolute_uri() + \
                livro_dict['capa'].url[1:]
        else:
            livro_dict['capa'] = ''

        del livro_dict['publicado']

        return JsonResponse(
            livro_dict,
            safe=False,
        )


class LivroListViewHomeApi(LivroListViewBase):
    template_name = 'livros/paginas/home.html'

    def render_to_response(self, context, **response_kwargs):
        livros = self.get_context_data()['livros']
        livros_list = livros.object_list.values()

        return JsonResponse(
            list(livros_list),
            safe=False
        )