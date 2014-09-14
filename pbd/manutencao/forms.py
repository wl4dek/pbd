from django import forms
from .models import Manuntencao
from django.utils.translation import ugettext as _


class ManutencaoForm(forms.ModelForm):
    data = forms.TimeField(label=_('Data'))
    valor_gasto = forms.DecimalField(label=_('Valor Gasto'),  max_digits=6,
                                     decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(ManutencaoForm, self).__init__(*args, **kwargs)
        self.fields['data'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_gasto'].widget.attrs.update({'class': 'form-control'})
        self.fields['produto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Manuntencao
        fields = ['data', 'valor_gasto', 'produto']
