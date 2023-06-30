from django.urls import path

from livros import views

app_name = "livros"

urlpatterns = [
    path('', views.home, name="home"), 
    path('livro/search/', views.search, name="search"),
    path('livro/category/<int:category_id>/', views.category, name="category"),
    path('livro/<int:id>/', views.livro, name="livro"),
    
]