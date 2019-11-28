from django import forms
from .models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router
from django.db.models import Q

ht = '* Поле обязательное для заполнения'


class LabelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "[sn: {0}] {1}".format(obj.id_sn, obj.model)


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
    unit_arm = LabelModelChoiceField(label='Системный блок',
                                      required=True,
                                      help_text=ht,
                                      queryset=Unit.objects.filter(Q(arm=False) | Q(arm=None)),
                                      empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    monitor_arm = LabelModelChoiceField(label='Монитор',
                                        required=True,
                                        help_text=ht,
                                        queryset=Monitor.objects.filter(Q(arm=False) | Q(arm=None)),
                                        empty_label=None,
                                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    printer_arm = LabelModelChoiceField(label='МФУ / Принтер',
                                        queryset=Printer.objects.filter(Q(arm=False) | Q(arm=None)),
                                        empty_label="",
                                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    scanner_arm = LabelModelChoiceField(label='Сканер',
                                        queryset=Scanner.objects.filter(Q(arm=False) | Q(arm=None)),
                                        empty_label="",
                                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    ibp_arm = LabelModelChoiceField(label='ИБП',
                                        queryset=IBP.objects.filter(Q(arm=False) | Q(arm=None)),
                                        empty_label="",
                                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    scale_arm = LabelModelChoiceField(label='Весы',
                                    queryset=Scale.objects.filter(Q(arm=False) | Q(arm=None)),
                                    empty_label="",
                                    widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    phone_arm = LabelModelChoiceField(label='Телефон',
                                      queryset=Phone.objects.filter(Q(arm=False) | Q(arm=None)),
                                      empty_label="",
                                      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
