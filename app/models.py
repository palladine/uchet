from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    roles = (
        ('1', 'Администратор'),
        ('2', 'Пользователь'),
    )
    role = models.CharField(max_length=100, default=2, choices=roles, verbose_name="Роль")


class ARM(models.Model):
    unit_arm = models.ForeignKey("Unit", default='', on_delete=models.CASCADE, null=False, blank=False, related_name='unit_arm_id', verbose_name="Системный блок")
    monitor_arm = models.ForeignKey("Monitor", default='', on_delete=models.CASCADE, null=False, blank=False, related_name='monitor_arm_id', verbose_name="Монитор")
    printer_arm = models.ForeignKey("Printer", on_delete=models.SET_NULL, null=True, blank=True, related_name='printer_arm_id', verbose_name="Принтер")
    scanner_arm = models.ForeignKey("Scanner", on_delete=models.SET_NULL, null=True, blank=True, related_name='scanner_arm_id', verbose_name="Сканер")
    ibp_arm = models.ForeignKey("IBP", on_delete=models.SET_NULL, null=True, blank=True, related_name='ibp_arm_id', verbose_name="ИБП")
    scale_arm = models.ForeignKey("Scale", on_delete=models.SET_NULL, null=True, blank=True, related_name='scale_arm_id', verbose_name="Весы")
    phone_arm = models.ForeignKey("Phone", on_delete=models.SET_NULL, null=True, blank=True, related_name='phone_arm_id', verbose_name="Телефон")
    comp_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Имя компьютера")
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="IP-адрес")
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = "АРМ"
        verbose_name_plural = "АРМы"

    def __str__(self):
        return "[{0}] {1}({2}/{3})".format(self.pk, self.unit_arm, self.comp_name, self.ip)


class Unit(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    memory = models.PositiveSmallIntegerField(default=0, null=True, blank=True, verbose_name="Память (Гб)")
    os = models.CharField(max_length=255, null=True, blank=True, verbose_name="Операционная система")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "Системный блок"
        verbose_name_plural = "Системные блоки"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Monitor(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "Монитор"
        verbose_name_plural = "Мониторы"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Printer(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="IP-адрес")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")


    class Meta:
        verbose_name = "МФУ / Принтер"
        verbose_name_plural = "МФУ / Принтеры"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Scanner(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    id_sn_base = models.CharField(max_length=100, null=True, blank=True, verbose_name="Серийный номер базы")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "Сканер"
        verbose_name_plural = "Сканеры"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class IBP(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "ИБП"
        verbose_name_plural = "ИБП"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Scale(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списаны")

    class Meta:
        verbose_name = "Весы"
        verbose_name_plural = "Весы"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Phone(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    #id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="IP-адрес")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)


class Router(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False, verbose_name="Модель")
    #id_naumen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер в Naumen")
    id_invent = models.CharField(max_length=255, null=True, blank=True, verbose_name="Инвентарный номер")
    id_sn = models.CharField(max_length=255, default='', null=False, blank=False, unique=True, verbose_name="Серийный номер")
    #arm = models.ForeignKey(ARM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="АРМ")
    ip = models.CharField(max_length=100, null=True, blank=True, verbose_name="IP-адрес")
    retired = models.BooleanField(default=False, null=True, blank=True, verbose_name="Списан")

    class Meta:
        verbose_name = "Маршрутизатор / Свич"
        verbose_name_plural = "Маршрутизаторы / Свичи"

    def __str__(self):
        return "[{0}] {1}".format(self.pk, self.model)