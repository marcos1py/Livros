from django.test import TestCase
from django.urls import resolve, reverse
from livros.models import Category, Livro, User
from datetime import datetime

from livros.views import site

class LivroViewsTest(TestCase):
    def test_livro_home_view_function_is_correct(self):
        view = resolve(reverse('livros:home'))
        self.assertIs(view.func, site.home)

    def test_livro_category_view_function_is_correct(self):
        view = resolve(reverse('livros:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, site.category)

    def test_livro_detail_view_function_is_correct(self):
        view = resolve(reverse('livros:livro', kwargs={'id': 1}))
        self.assertIs(view.func, site.livro)

    def test_livro_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('livros:home'))
        self.assertEqual(response.status_code, 200)

    def test_livro_home_view_loads_correct_template(self):
        response = self.client.get(reverse('livros:home'))
        self.assertTemplateUsed(response, 'livros/paginas/home.html')
        
    def test_livro_home_template_shows_no_livros_found_if_no_livros(self):
        response = self.client.get(reverse('livros:home'))
        self.assertIn(
            '<h1>Nenhum livro encontrado aqui 🥲</h1>',
            response.content.decode('utf-8')
        )


    def test_livro_category_view_function_is_correct(self):
        view = resolve(
            reverse('livros:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, site.category)



    def test_livro_detail_view_function_is_correct(self):
        view = resolve(
            reverse('livros:livro', kwargs={'id': 1})
        )
        self.assertIs(view.func, site.livro)

    def test_livro_detail_view_returns_404_if_no_livros_found(self):
        response = self.client.get(
            reverse('livros:livro', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)



    def test_livro_search_uses_correct_view_function(self):
        resolved = resolve(reverse('livros:search'))
        self.assertIs(resolved.func, site.search)

