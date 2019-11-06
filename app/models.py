from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    roles = (
        ('1', 'Администратор'),
        ('2', 'Пользователь'),
    )
    role = models.CharField(max_length=100, default=2, choices=roles, verbose_name="Роль")


class ARM(models.Model):
    # ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="IP-адрес")
    # computer_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Имя компьютера")
    ...


class Unit(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    memory = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Память")
    os = models.CharField(max_length=255, null=True, blank=True, verbose_name="Операционная система")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, blank=False, null=False, verbose_name="Списан")


    class Meta:
        verbose_name = "Системный блок"
        verbose_name_plural = "Системные блоки"