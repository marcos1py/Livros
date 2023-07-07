from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib import messages
from .forms import LoginForm, RegistrarForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from livros.models import Livro

def registrar_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegistrarForm(register_form_data)
    return render(request, 'authors/paginas/registrar_view.html', context={
        "form": form,
        'form_action': reverse('authors:register_create'),
    })

def registrar_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegistrarForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "User criador com sucesso")
        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))
    return redirect('authors:registrar')


def login_view(request):
    form = LoginForm()
    return render(request, "authors/paginas/login.html", {
        'form': form,
        'form_action': reverse('authors:login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(reverse('authors:dashboard'))


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request')
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return redirect(reverse('authors:login'))

    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    livros = Livro.objects.filter(
        publicado = False,
        author=request.user
    )
    
    return render(request, 'authors/paginas/dashboard.html', context={
        "livros":livros,
    })