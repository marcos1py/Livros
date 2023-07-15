from authors.forms.livro_form import AuthorlivroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from livros.models import Livro


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class Dashboardlivro(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_livro(self, id=None):
        livro = None

        if id is not None:
            livro = Livro.objects.filter(
               
                author=self.request.user,
                pk=id,
            ).first()

            if not livro:
                raise Http404()

        return livro

    def render_livro(self, form):
        return render(
            self.request,
            'authors/paginas/dashboard_livro.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        livro = self.get_livro(id)
        form = AuthorlivroForm(instance=livro)
        return self.render_livro(form)

    def post(self, request, id=None):
        livro = self.get_livro(id)
        form = AuthorlivroForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=livro
        )

        if form.is_valid():
            # Agora, o form é válido e eu posso tentar salvar
            livro = form.save(commit=False)

            livro.author = request.user
            
            livro.publicado = False

            livro.save()

            messages.success(request, 'Sua  foi salva com sucesso!')
            return redirect(
                reverse(
                    'authors:dashboard_livro_edit', args=(
                        livro.id,
                    )
                )
            )

        return self.render_livro(form)
    
@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardlivroDelete(Dashboardlivro):
    def post(self, *args, **kwargs):
        livro = self.get_livro(self.request.POST.get('id'))
        livro.delete()
        messages.success(self.request, 'Deleted successfully.')
        return redirect(reverse('authors:dashboard'))