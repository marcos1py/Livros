from django.urls import path

from livros import views

app_name = "livros"

urlpatterns = [
    path('', views.home, name="home"), 
    path('livro/<int:id>/', views.livro, name="livro"),
]