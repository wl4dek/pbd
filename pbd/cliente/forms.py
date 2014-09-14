from django import forms
from pbd.accounts.forms import UsuarioForm
from .models import Cliente
from django.utils.translation import ugettext as _


class ClienteForm(UsuarioForm):
    locatario = forms.CharField(label=_('Locatario'), required=True)
    cnpj = forms.CharField(label=_('CNPJ'), required=True)
    rg = forms.CharField(label=_('RG'), max_length=14, required=True)
    municipio = forms.CharField(label=_('Inscrição Municipal'),
                                max_length=200, required=True)
    contato = forms.CharField(label=_('Contato'), max_length=200,
                              required=True)

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['locatario'].widget.attrs.update({'class': 'form-control'})
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control'})
        self.fields['rg'].widget.attrs.update({'class': 'form-control'})
        self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
        self.fields['contato'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'cpf', 'endereco', 'bairro', 'cidade',
                  'estado', 'cep', 'locatario', 'cnpj', 'rg', 'municipio',
                  'contato']
