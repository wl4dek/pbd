from django import forms
from .models import Produto
from django.utils.translation import ugettext as _


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label=_('Nome'), max_length=45)
    quantidade = forms.IntegerField(label=_('Quantidade'))
    valor_venda = forms.DecimalField(label=_('Valor de Venda'))
    valor_locacao = forms.DecimalField(label=_('Valor de Locação'))

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_venda'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_locacao'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'valor_venda', 'valor_locacao']
