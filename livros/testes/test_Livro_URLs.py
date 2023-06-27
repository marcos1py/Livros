
from django.test import TestCase
from django.urls import reverse


class LivroURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Um é igual a um'

    def testa_livro_home_url_esta_correta(self):
        url = reverse('livros:home')
        self.assertEqual(url, '/')

    def test_livro_category_url_esta_correta(self):
        url = reverse('livros:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/livro/category/1/')

    def test_livro_detail_url_esta_correta(self):
        url = reverse('livros:livro', kwargs={'id': 1})
        self.assertEqual(url, '/livro/1/')