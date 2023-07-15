from django.urls import path

from livros import views

app_name = "livros"

urlpatterns = [
    path('', views.LivroListViewBase.as_view(), name="home"),
    path(
        'livros/search/',
        views.LivroListViewSearch.as_view(), name="search"
    ),
    path(
        'livros/category/<int:category_id>/',
        views.LivroListViewCategory.as_view(), name="category"
    ),
    
    path(
        'livros/<int:pk>/',
        views.LivroDetail.as_view(),
        name="livro"
    ),
    
    path(
        'livros/api/v1/',
        views.LivroListViewHomeApi.as_view(),
        name="livros_api_v1",
    ),
    path(
        'livros/api/v1/<int:pk>/',
        views.LivroDetailAPI.as_view(),
        name="livros_api_v1_detail",
    ),
    path(
        'livros/api/v2/',
        views.livro_api_list,
        name='livros_api_v2'
    ),
]