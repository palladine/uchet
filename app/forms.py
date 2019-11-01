from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Имя пользователя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))

class AddUnitForm(forms.Form):
    ht = '* Поле обязательное для заполнения'

    OS_CHOICES = (
        (1, ("")),
        (2, ("Win XP (32 bit)")),
        (3, ("Win XP (64 bit)")),
        (4, ("Win 7 (32 bit)")),
        (5, ("Win 7 (64 bit)"))
    )

    model = forms.CharField(label='Модель', help_text=ht, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    memory = forms.IntegerField(label='Память (Гб)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    os = forms.ChoiceField(label='Операционная система', required=False, choices=OS_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    id_naumen = forms.CharField(label='Номер в Naumen', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_invent = forms.CharField(label='Инвентарный номер', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    id_sn = forms.CharField(label='Серийный номер', help_text=ht, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm required'}))
    retired = forms.BooleanField(label="Списан", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))
    active = forms.BooleanField(label="Используется", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))