from unittest import TestCase

from ultils.livros.paginaçao import   criar_paginacao

class TestePaginacao(TestCase):
    def test_make_pagination_range_retorna_um_intervalo_de_paginacao(self):
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=1,
        )['paginacao']
        self.assertEqual([1, 2, 3, 4], paginacao)

    def test_primeiro_intervalo_e_statico_se_pagina_atual_for_menor_que_pagina_do_meio(self):  # noqa: E501
        # Página atual = 1 - Qtde de páginas = 2 - Página do meio = 2
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=1,
        )['paginacao']
        self.assertEqual([1, 2, 3, 4], paginacao)

        # Página atual = 2 - Qtde de páginas = 2 - Página do meio = 2
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=2,
        )['paginacao']
        self.assertEqual([1, 2, 3, 4], paginacao)

        # Página atual = 3 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=3,
        )['paginacao']
        self.assertEqual([2, 3, 4, 5], paginacao)

        # Página atual = 4 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=4,
        )['paginacao']
        self.assertEqual([3, 4, 5, 6], paginacao)

    def test_asegurar_que_os_intervalos_do_meio_estao_corretos(self):
        # Página atual = 10 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=10,
        )['paginacao']
        self.assertEqual([9, 10, 11, 12], paginacao)

        # Página atual = 14 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=12,
        )['paginacao']
        self.assertEqual([11, 12, 13, 14], paginacao)

    def test_make_pagination_range_e_statico_quando_ultima_pagina_e_a_proxima(self):
        # Página atual = 18 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=18,
        )['paginacao']
        self.assertEqual([17, 18, 19, 20], paginacao)

        # Página atual = 19 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=19,
        )['paginacao']
        self.assertEqual([17, 18, 19, 20], paginacao)

        # Página atual = 20 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=20,
        )['paginacao']
        self.assertEqual([17, 18, 19, 20], paginacao)

        # Página atual = 21 - Qtde de páginas = 2 - Página do meio = 2
        # AQUI O INTERVALO DEVE MUDAR
        paginacao =  criar_paginacao(
            intervalo_paginas=list(range(1, 21)),
            qtde_paginas=4,
            pagina_atual=21,
        )['paginacao']
        self.assertEqual([17, 18, 19, 20], paginacao)
