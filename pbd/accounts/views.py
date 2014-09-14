from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login


def entrar(request):
    if request.user.is_authenticated():
        return redirect('core:home')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('core:home')
        else:
            return render(request, "login.html", {"form": form})

    return render(request, "login.html", {"form": LoginForm()})
