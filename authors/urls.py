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
    path(
        'dashboard/livro/new/',
        views.Dashboardlivro.as_view(),
        name='dashboard_livro_new'
    ),
    path(
        'dashboard/livro/delete/',
        views.DashboardlivroDelete.as_view(),
        name='dashboard_livro_delete'
    ),
    path(
        'dashboard/livro/<int:id>/edit/',
        views.Dashboardlivro.as_view(),
        name='dashboard_livro_edit'
    ),
    path(
        'profile/<int:id>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
]