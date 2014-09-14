from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Telefone(models.Model):
    telefone = models.CharField(_('Telefone'), max_length=18)

    class Meta:
        verbose_name = _('Telefone')
        verbose_name_plural = _('Telefones')
        ordering = ['telefone']


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Nome'), unique=True, max_length=45,
                                blank=False)
    email = models.EmailField(_('E-mail'), unique=True, blank=False)
    endereco = models.CharField(_('Endereço'), max_length=200, blank=True)
    bairro = models.CharField(_('Bairro'), max_length=200, blank=True)
    cidade = models.CharField(_('Cidade'), max_length=100, blank=True)
    estado = models.CharField(_('Estado'), max_length=100, blank=True)
    cep = models.CharField(_('CEP'), max_length=10, blank=True)
    cpf = models.CharField(_('CPF'), max_length=14, unique=True, blank=True)
    telefones = models.ManyToManyField(Telefone)

    is_active = models.BooleanField(_('Está ativo?'), blank=True, default=True)
    is_staff = models.BooleanField(_('É da equipe?'), blank=True,
                                   default=False)
    date_joined = models.DateTimeField(_('Data de Entrada'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        ordering = ['username']


class PasswordReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Usuário'),
        related_name=_('resets'))

    key = models.CharField(_('Chave'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)

    confirmed = models.BooleanField(
        _('Confirmado?'),
        default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

        class Meta:
            verbose_name = _('Usuário')
            verbose_name_plural = _('Usuários')
            ordering = ['-created_at']
