from django import forms
from pbd.accounts.forms import UsuarioForm
from .models import Funcionario
from django.utils.translation import ugettext as _


class FuncionarioForm(UsuarioForm):
    salario = forms.DecimalField(label=_('Salário'), max_digits=6,
                                 decimal_places=2, required=True)
    funcao = forms.CharField(label=_('Função'), max_length=45)
    password1 = forms.CharField(label=_('Senha'),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Confirmação de Senha'),
                                widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(FuncionarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_staff = False
        if commit:
            user.save()
            #Adiciona no seu respectivo gurpo
            #group = Group.objects.get(name='Secretarias')
            #user.groups.add(group)

        return user

    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['salario'].widget.attrs.update({'class': 'form-control'})
        self.fields['funcao'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'cpf', 'funcao', 'endereco', 'bairro',
                  'cidade', 'estado', 'cep', 'salario']
