from django.shortcuts import render, get_object_or_404, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar(request):
    template_name = 'view/inscricao.html'
    context = {}

    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.save()
        form = FuncionarioForm(None)

    context['form'] = form
    context['title'] = 'Inscrição de Funcionários'
    return render(request, template_name, context)


@login_required
def listar(request):
    template_name = 'view/listar.html'
    context = {}

    context['objetos'] = Funcionario.objects.all()
    context['title'] = 'Funcionarios'
    return render(request, template_name, context)


@login_required
def editar(request, pk):
    template_name = 'view/editar.html'
    context = {}

    funcionario = get_object_or_404(Funcionario, pk=pk)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            form.save()
            # messages.success(
            #     request, 'Aluno editado com sucesso!'
            # )
            return redirect('funcionario:listar')
    else:
        form = FuncionarioForm(instance=funcionario)

    context['form'] = form
    context['title'] = funcionario
    return render(request, template_name, context)
