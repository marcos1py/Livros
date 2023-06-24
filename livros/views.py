from django.shortcuts import render
from django.http import HttpResponse
from ultils.livros.fabrica_de_livros import make_livro

def home(request):
   return render(request, "livros/paginas/home.html", context={
      "livros":[make_livro() for _ in  range(10)],
      })

def livro(request, id):
   return render(request, "livros/paginas/livro-view.html", context={
      "livro":make_livro(),
      "detalhe_da_pagina":True,
      })