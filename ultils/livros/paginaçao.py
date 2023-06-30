import math
from django.core.paginator import Paginator


def criar_paginacao( intervalo_paginas, qtde_paginas, pagina_atual):

    intervalo_meio = math.ceil(qtde_paginas / 2)
    inicio_intervalo = pagina_atual - intervalo_meio
    fim_intervalo = pagina_atual + intervalo_meio
    total_paginas = len(intervalo_paginas)

    deslocamento_inicio_intervalo = abs(inicio_intervalo) if inicio_intervalo < 0 else 0

    if inicio_intervalo < 0:
        inicio_intervalo = 0
        fim_intervalo += deslocamento_inicio_intervalo

    if fim_intervalo >= total_paginas:
        inicio_intervalo = inicio_intervalo - abs(total_paginas-fim_intervalo)

    paginacao = intervalo_paginas[inicio_intervalo:fim_intervalo]
    return {
        'paginacao': paginacao,
        'intervalo_paginas': intervalo_paginas,
        'qtde_paginas': qtde_paginas,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'inicio_intervalo': inicio_intervalo,
        'fim_intervalo': fim_intervalo,
        'primeira_pagina_fora_do_intervalo': pagina_atual > intervalo_meio,
        'ultima_pagina_fora_do_intervalo': fim_intervalo < total_paginas,
    }


def paginaçao_das_page(request, livros, per_page, qty_pages=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(livros, per_page)
    pagina_obj = paginator.get_page(current_page)

    pagination_range = criar_paginacao(
        paginator.page_range,
        qty_pages,
        current_page
    )
    return pagina_obj, pagination_range