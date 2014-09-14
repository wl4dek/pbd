from django.shortcuts import render
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar(request):
    template_name = 'view/inscricao.html'
    context = {}

    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.save()
        form = ProdutoForm(None)

    context['form'] = form
    context['title'] = 'Inscrição de Produto'
    return render(request, template_name, context)
