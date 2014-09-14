from django.db import models
from pbd.cliente.models import Cliente
from pbd.produto.models import Produto
from django.utils.translation import ugettext_lazy as _


class Contrato(models.Model):
    entrega = models.DateTimeField(_('Data de Entrega'), auto_now_add=True)
    hora = models.TimeField(_('Hora'))
    duracao = models.DateTimeField(_('Duração'), blank=False)
    referencia = models.CharField(_('Referência Obra'), max_length=200,
                                  blank=True)
    endereco = models.CharField(_('Endereço Obra'), max_length=200, blank=True)
    bairro = models.CharField(_('Bairro da Obra'), max_length=200, blank=True)
    cidade = models.CharField(_('Cidade da Obra'), max_length=100, blank=True)
    estado = models.CharField(_('Estado da Obra'), max_length=100, blank=True)
    cep = models.CharField(_('CEP da Obra'), max_length=10, blank=True)
    desconto = models.DecimalField(_('Valor Locação'), blank=True,
                                   max_digits=5, decimal_places=2)
    valor_contrato = models.DecimalField(_('Valor Contrato'), blank=True,
                                         max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, blank=True, related_name='Cliente')
    produto = models.ManyToManyField(Produto, blank=True,
                                     related_name='Produtos')

    class Meta:
        verbose_name = _('Contrato')
        verbose_name_plural = _('Contratos')
        ordering = ['cliente']
