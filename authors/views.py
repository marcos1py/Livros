from django.shortcuts import render


def registrar_view(request):
    return render(request, 'authors/paginas/registrar_view.html')