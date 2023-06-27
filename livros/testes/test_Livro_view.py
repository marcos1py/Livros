from django.test import TestCase
from django.urls import resolve, reverse
from livros.models import Category, Livro, User
from datetime import datetime

from livros import views

class LivroViewsTest(TestCase):
    def test_livro_home_view_function_is_correct(self):
        view = resolve(reverse('livros:home'))
        self.assertIs(view.func, views.home)

    def test_livro_category_view_function_is_correct(self):
        view = resolve(reverse('livros:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_livro_detail_view_function_is_correct(self):
        view = resolve(reverse('livros:livro', kwargs={'id': 1}))
        self.assertIs(view.func, views.livro)

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

    def test_livro_home_template_loads_livro(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        data_publicacao = datetime.strptime('2023/04/19', '%Y/%m/%d').date()
        livro = Livro.objects.create(
            category=category,
            author=author,
            titulo="PEQUENO PRINCIPE",
            descricao1="PEQUENO PRINCIPE DESCRICAO 1",
            descricao2="PEQUENO PRINCIPE DESCRICAO 2",
            slug="PEQUENO-PRINCIPE",
            total_de_paginas="100",
            data_publicacao= data_publicacao,
            publicado=True,
        )
        response = self.client.get(reverse('livros:home'))
        content = response.content.decode('utf-8')
        response_context_livros = response.context['livros']

        self.assertIn('PEQUENO PRINCIPE', content)
        self.assertIn("PEQUENO PRINCIPE DESCRICAO 1", content)
        self.assertIn("PEQUENO PRINCIPE DESCRICAO 2", content)
        self.assertEqual(len(response_context_livros), 1)

    def test_livro_category_view_function_is_correct(self):
        view = resolve(
            reverse('livros:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)



    def test_livro_detail_view_function_is_correct(self):
        view = resolve(
            reverse('livros:livro', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.livro)

    def test_livro_detail_view_returns_404_if_no_livros_found(self):
        response = self.client.get(
            reverse('livros:livro', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
