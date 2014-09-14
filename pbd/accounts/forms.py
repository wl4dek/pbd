from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Telefone
from .models import User
from django.utils.translation import ugettext as _
#Form inline para o telefone

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Nome')})
    )
    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Senha')})
    )


class TelefoneForm(forms.ModelForm):
    """docstring for TelefoneForm"""
    telefone = forms.CharField(label=_('Telefone'), max_length=15)

    def __init__(self, *args, **kwargs):
        super(TelefoneForm, self).__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Telefone
        fields = ['telefone']


class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label=_('Nome'), required=True)
    email = forms.EmailField(label=_('E-mail'), required=True)
    cpf = forms.CharField(label=_('CPF'), max_length=14, required=True)
    endereco = forms.CharField(label=_('Endereço'), max_length=200,
                               required=True)
    bairro = forms.CharField(label=_('Bairro'), max_length=200, required=True)
    cidade = forms.CharField(label=_('Cidade'), max_length=100, required=True)
    estado = forms.CharField(label=_('Estado'), max_length=100, required=True)
    cep = forms.CharField(label=_('CEP'), max_length=10, required=True)

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'cpf', 'endereco', 'bairro', 'cidade',
                  'estado', 'cep']
