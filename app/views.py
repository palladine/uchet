from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Unit, Monitor, Printer, Scanner
from django.views import View
from .forms import LoginForm, AddUnitForm, AddMonitorForm, AddPrinterForm, AddScannerForm
from django.urls import reverse



class UserLoginRegistration(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            context = {'form': form}
            return render(request, 'login.html', context=context)
        else:
            return HttpResponseRedirect(reverse('home'))


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']

            if 'enter' in request.POST:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    error = 'Пользователь с именем \'{}\' не зарегистрирован.'.format(username)
                    context = {'form': form, 'error': error}
                    return render(request, 'login.html', context=context)

            elif 'registration' in request.POST:
                new_user = User.objects.create_user(username, '', password)
                new_user.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))

        else:
            context = {'form': form}
            return render(request, 'login.html', context=context)



class UserLogout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))




class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {'user': request.user, 'title': 'Главная'}

            return render(request, 'home.html', context=context)
        else:
            return HttpResponseRedirect(reverse('login'))


class AddItem(View):
    def get(self, request, item):
        context = {}
        if item == 'unit':
            form = AddUnitForm()
            context.update({'title': 'Добавление системного блока', 'form': form, 'item': item})

        if item == 'monitor':
            form = AddMonitorForm()
            context.update({'title': 'Добавление монитора', 'form': form, 'item': item})

        if item == 'printer':
            form = AddPrinterForm()
            context.update({'title': 'Добавление МФУ / принтера', 'form': form, 'item': item})

        if item == 'scanner':
            form = AddScannerForm()
            context.update({'title': 'Добавление сканера', 'form': form, 'item': item})

        return render(request, 'add_item.html', context=context)


    def post(self, request, item):
        dic_forms = {'unit': AddUnitForm(request.POST), 'monitor': AddMonitorForm(request.POST),
                     'printer': AddPrinterForm(request.POST), 'scanner': AddScannerForm(request.POST)}
        form = dic_forms[item]
        context = {'form': form, 'item': item}

        if form.is_valid():

            if item == 'unit':
                model = request.POST.get('model')
                memory = request.POST.get('memory')
                os = request.POST.get('os')
                id_naumen = request.POST.get('id_naumen')
                id_invent = request.POST.get('id_invent')
                id_sn = request.POST.get('id_sn')
                retired = request.POST.get('retired')
                unit_item = Unit(model=model, id_sn=id_sn)
                unit_item.memory = memory if memory else 0
                unit_item.os = os
                unit_item.id_naumen = id_naumen
                unit_item.id_invent = id_invent
                unit_item.retired = True if retired else False
                unit_item.save()
                messages.success(request, 'Системный блок добавлен')


            if item == 'monitor':
                model = request.POST.get('model')
                id_naumen = request.POST.get('id_naumen')
                id_invent = request.POST.get('id_invent')
                id_sn = request.POST.get('id_sn')
                retired = request.POST.get('retired')
                monitor_item = Monitor(model=model, id_sn=id_sn)
                monitor_item.id_naumen = id_naumen
                monitor_item.id_invent = id_invent
                monitor_item.retired = True if retired else False
                monitor_item.save()
                messages.success(request, 'Монитор добавлен')


            if item == 'printer':
                model = request.POST.get('model')
                id_naumen = request.POST.get('id_naumen')
                id_invent = request.POST.get('id_invent')
                id_sn = request.POST.get('id_sn')
                ip = request.POST.get('ip')
                retired = request.POST.get('retired')
                printer_item = Printer(model=model, id_sn=id_sn)
                printer_item.id_naumen = id_naumen
                printer_item.id_invent = id_invent
                printer_item.ip = ip
                printer_item.retired = True if retired else False
                printer_item.save()
                messages.success(request, 'МФУ / принтер добавлен')

            if item == 'scanner':
                model = request.POST.get('model')
                id_naumen = request.POST.get('id_naumen')
                id_invent = request.POST.get('id_invent')
                id_sn = request.POST.get('id_sn')
                id_sn_base = request.POST.get('id_sn_base')
                retired = request.POST.get('retired')
                scanner_item = Scanner(model=model, id_sn=id_sn)
                scanner_item.id_naumen = id_naumen
                scanner_item.id_invent = id_invent
                scanner_item.id_sn_base = id_sn_base
                scanner_item.retired = True if retired else False
                scanner_item.save()
                messages.success(request, 'Сканер добавлен')

            return HttpResponseRedirect(reverse('add_item', args=(item,)))
        else:
            messages.error(request, form.errors)
        return render(request, 'add_item.html', context=context)





class ShowItems(View):
    def get(self, request, items):
        context = {}
        if items == 'units':
            context = {'title': 'Системные блоки'}
        return render(request, 'show_items.html', context=context)
