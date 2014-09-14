from django.db import models
from django.utils.translation import ugettext_lazy as _
from pbd.accounts.models import User


class Cliente(User):
    locatario = models.CharField(_('Locatário'), max_length=45)
    cnpj = models.CharField(_('CNPJ'), max_length=18)
    rg = models.CharField(_('RG'), max_length=45)
    municipio = models.CharField(_('Insc. Municípal'), max_length=45)
    contato = models.CharField(_('Contato'), max_length=45)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ['username']
