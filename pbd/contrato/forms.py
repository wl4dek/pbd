from django import forms
from .models import Contrato
from django.utils.translation import ugettext as _


class ContratoForm(forms.ModelForm):
    entrega = forms.DateTimeField(label=_('Data de Entrega'), required=True)
    duracao = forms.DateTimeField(label=_('Duração'))
    referencia = forms.CharField(label=_('Referencia da Obra'), max_length=200)
    endereco = forms.CharField(label=_('Endereço da Obra'), max_length=200)
    bairro = forms.CharField(label=_('Bairro da Obra'), max_length=200)
    cep = forms.CharField(label=_('CEP da Obra'), max_length=200)
    hora = forms.TimeField(label=_('Hora'))
    desconto = forms.DecimalField(_('Valor Locação'), max_digits=5,
                                  decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(ContratoForm, self).__init__(*args, **kwargs)
        self.fields['entrega'].widget.attrs.update({'class': 'form-control'})
        self.fields['duracao'].widget.attrs.update({'class': 'form-control'})
        self.fields['referencia'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control'})
        self.fields['hora'].widget.attrs.update({'class': 'form-control'})
        self.fields['desconto'].widget.attrs.update({'class': 'form-control'})
        self.fields['cliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['produto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contrato
        fields = ['entrega', 'duracao', 'referencia', 'endereco', 'bairro',
                  'cep', 'hora', 'desconto', 'cliente', 'produto']
