from django.shortcuts import render
from .forms import ManutencaoForm
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar(request):
    template_name = 'view/inscricao.html'
    context = {}

    form = ManutencaoForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.save()
        form = ManutencaoForm(None)

    context['form'] = form
    context['title'] = 'Inscrição de Manuntenção'
    return render(request, template_name, context)
