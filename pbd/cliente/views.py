from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar(request):
    template_name = 'view/inscricao.html'
    context = {}

    form = ClienteForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.save()
        form = ClienteForm(None)

    context['form'] = form
    context['title'] = 'Inscrição de Cliente'
    return render(request, template_name, context)


@login_required
def listar(request):
    template_name = 'view/listar.html'
    context = {}

    context['objetos'] = Cliente.objects.all()
    context['title'] = 'Clientes'
    return render(request, template_name, context)


@login_required
def editar(request, pk):
    template_name = 'view/editar.html'
    context = {}

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            # messages.success(
            #     request, 'Aluno editado com sucesso!'
            # )
            return redirect('cliente:listar')
    else:
        form = ClienteForm(instance=cliente)

    context['form'] = form
    context['title'] = cliente
    return render(request, template_name, context)
