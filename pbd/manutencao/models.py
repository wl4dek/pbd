from django.db import models
from pbd.produto.models import Produto
from django.utils.translation import ugettext_lazy as _


class Manuntencao(models.Model):
    data = models.DateTimeField(_('Data'))
    valor_gasto = models.DecimalField(_('Valor Gasto'), max_digits=6,
                                      decimal_places=2, blank=True)
    obs = models.TextField(_('Obs'))
    produto = models.ForeignKey(Produto)

    class Meta:
        verbose_name = _('Manunteção')
        verbose_name_plural = _('Manunteções')
        ordering = ['produto']
