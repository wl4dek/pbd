from django.shortcuts import render
from .forms import ContratoForm
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar(request):
    template_name = 'view/inscricao.html'
    context = {}

    form = ContratoForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.save()
        form = ContratoForm(None)

    context['form'] = form
    context['title'] = 'Criando Contrato'
    return render(request, template_name, context)
