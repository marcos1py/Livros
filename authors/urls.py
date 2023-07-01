from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path('registrar/', views.registrar_view, name='registrar'),
    path('registrar/create/', views.registrar_create, name='create'),
]