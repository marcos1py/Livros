from django.shortcuts import render,redirect
from .forms import RegistrarForm
from django.http import Http404
from django.contrib import messages

def registrar_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = ReguistrarForm(register_form_data)

    return render(request, 'authors/paginas/registrar_view.html', context={
        "form": form,
    })

def registrar_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = ReguistrarForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, "User criador com sucesso")
        del(request.session['register_form_data'])
        

    return redirect('authors:registrar')
