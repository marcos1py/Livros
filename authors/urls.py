from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path('registrar/', views.registrar_view, name='registrar'),
    path('register/create/', views.registrar_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]