from django import forms
from .models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router

ht = '* Поле обязательное для заполнения'


class LoginForm(forms.Form):
    login = forms.CharField(label='Имя пользователя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))


class AddUnitForm(forms.Form):
    OS_CHOICES = (
        (" ", ("")),
        ("Win XP (32)", ("Win XP (32)")),
        ("Win XP (64)", ("Win XP (64)")),
        ("Win 7 (32)", ("Win 7 (32)")),
        ("Win 7 (64)", ("Win 7 (64)"))
    )
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    memory = forms.IntegerField(label='Память (Гб)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    os = forms.CharField(label='Операционная система', required=False, widget=forms.Select(choices=OS_CHOICES, attrs={'class': 'form-control form-control-sm'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddMonitorForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddPrinterForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    ip = forms.CharField(label="IP-адрес", required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddScannerForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_sn_base = forms.CharField(label="Серийный номер базы", required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddIBPForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddScaleForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    retired = forms.BooleanField(label="Списаны", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddPhoneForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    #id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    ip = forms.CharField(label="IP-адрес", required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddRouterForm(forms.Form):
    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    #id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    ip = forms.CharField(label="IP-адрес", required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class AddARMForm(forms.Form):
    # todo objects.all() ---> filter(arm=False and arm= None)
    #unit_arm = forms.CharField(label='Системный блок', required=True, help_text=ht,
    #                             widget=forms.Select(choices=[(x.pk, "[sn: {0}] {1}".format(x.id_sn, x.model)) for x in Unit.objects.all()],
    #                                                 attrs={'class': 'form-control form-control-sm'}))
    unit_arm = forms.ModelChoiceField(label='Системный блок',
                                      required=True,
                                      help_text=ht,
                                      queryset=Unit.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    monitor_arm = forms.ModelChoiceField(label='Монитор',
                                      required=True,
                                      help_text=ht,
                                      queryset=Monitor.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

