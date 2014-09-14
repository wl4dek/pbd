from django.db import models
from pbd.accounts.models import User
from django.utils.translation import ugettext_lazy as _


class Funcionario(User):

    """Banco de dados Funcionário"""
    salario = models.DecimalField(_('Salário'), max_digits=6, decimal_places=2,
                                  blank=True)
    funcao = models.CharField(_('Funçao'), max_length=45, blank=True)

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
        ordering = ['username']
