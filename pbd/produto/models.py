from django.db import models
from django.utils.translation import ugettext_lazy as _


class Produto(models.Model):
    nome = models.CharField(_('Nome'), max_length=45, blank=False)
    quantidade = models.IntegerField(_('Quantidade'), blank=False)
    valor_venda = models.DecimalField(_('Valor Venda'), blank=True,
                                      max_digits=5, decimal_places=2)
    valor_locacao = models.DecimalField(_('Valor Locação'), blank=True,
                                        max_digits=5, decimal_places=2)
    date_joined = models.DateTimeField(_('Data de Entrada'), auto_now_add=True)

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')
        ordering = ['nome']
