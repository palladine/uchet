from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM
from django.views import View
from .forms import LoginForm, AddUnitForm, AddMonitorForm, AddPrinterForm, AddScannerForm, AddIBPForm, AddScaleForm, AddPhoneForm, AddRouterForm, AddARMForm
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

        status = request.session.get('status', False)
        msg = request.session.get('msg', False)

        request.session['status'] = False
        request.session['msg'] = False
        context.update({'status': status, 'msg': msg})

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

        if item == 'ibp':
            form = AddIBPForm()
            context.update({'title': 'Добавление ИБП', 'form': form, 'item': item})

        if item == 'scale':
            form = AddScaleForm()
            context.update({'title': 'Добавление весов', 'form': form, 'item': item})

        if item == 'phone':
            form = AddPhoneForm()
            context.update({'title': 'Добавление телефона', 'form': form, 'item': item})

        if item == 'router':
            form = AddRouterForm()
            context.update({'title': 'Добавление маршрутизатора / свича', 'form': form, 'item': item})

        if item == 'arm':
            form = AddARMForm()
            context.update({'title': 'Добавление АРМ', 'form': form, 'item': item})

        return render(request, 'add_item.html', context=context)


    def post(self, request, item):
        dic_forms = {'unit': AddUnitForm(request.POST), 'monitor': AddMonitorForm(request.POST),
                     'printer': AddPrinterForm(request.POST), 'scanner': AddScannerForm(request.POST),
                     'ibp': AddIBPForm(request.POST), 'scale': AddScaleForm(request.POST),
                     'phone': AddPhoneForm(request.POST), 'router': AddRouterForm(request.POST),
                     'arm': AddARMForm(request.POST)}
        form = dic_forms[item]
        context = {'form': form, 'item': item}


        if form.is_valid():
            model = request.POST.get('model')
            id_naumen = request.POST.get('id_naumen')
            id_invent = request.POST.get('id_invent')
            id_sn = request.POST.get('id_sn')
            retired = request.POST.get('retired')

            if item == 'unit':
                memory = request.POST.get('memory')
                os = request.POST.get('os')
                unit_item = Unit(model=model, id_sn=id_sn)
                unit_item.memory = memory if memory else 0
                unit_item.os = os
                unit_item.id_naumen = id_naumen
                unit_item.id_invent = id_invent
                unit_item.retired = True if retired else False
                unit_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Системный блок добавлен'

            if item == 'monitor':
                monitor_item = Monitor(model=model, id_sn=id_sn)
                monitor_item.id_naumen = id_naumen
                monitor_item.id_invent = id_invent
                monitor_item.retired = True if retired else False
                monitor_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Монитор добавлен'

            if item == 'printer':
                ip = request.POST.get('ip')
                printer_item = Printer(model=model, id_sn=id_sn)
                printer_item.id_naumen = id_naumen
                printer_item.id_invent = id_invent
                printer_item.ip = ip
                printer_item.retired = True if retired else False
                printer_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'МФУ / принтер добавлен'

            if item == 'scanner':
                id_sn_base = request.POST.get('id_sn_base')
                scanner_item = Scanner(model=model, id_sn=id_sn)
                scanner_item.id_naumen = id_naumen
                scanner_item.id_invent = id_invent
                scanner_item.id_sn_base = id_sn_base
                scanner_item.retired = True if retired else False
                scanner_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Сканер добавлен'

            if item == 'ibp':
                ibp_item = IBP(model=model, id_sn=id_sn)
                ibp_item.id_naumen = id_naumen
                ibp_item.id_invent = id_invent
                ibp_item.retired = True if retired else False
                ibp_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'ИБП добавлен'

            if item == 'scale':
                scale_item = Scale(model=model, id_sn=id_sn)
                scale_item.id_naumen = id_naumen
                scale_item.id_invent = id_invent
                scale_item.retired = True if retired else False
                scale_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Весы добавлены'

            if item == 'phone':
                ip = request.POST.get('ip')
                phone_item = Phone(model=model, id_sn=id_sn)
                #phone_item.id_naumen = id_naumen
                phone_item.id_invent = id_invent
                phone_item.ip = ip
                phone_item.retired = True if retired else False
                phone_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Телефон добавлен'

            if item == 'router':
                ip = request.POST.get('ip')
                router_item = Router(model=model, id_sn=id_sn)
                #router_item.id_naumen = id_naumen
                router_item.id_invent = id_invent
                router_item.ip = ip
                router_item.retired = True if retired else False
                router_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'Маршрутизатор / свич добавлен'

            if item == 'arm':
                unit_arm_id = request.POST.get('unit_arm')
                monitor_arm_id = request.POST.get('monitor_arm')
                arm_item = ARM()
                arm_item.unit_arm = Unit.objects.get(pk=unit_arm_id)
                arm_item.monitor_arm = Monitor.objects.get(pk=monitor_arm_id)
                # todo save arm field in Unit and Monitor items
                arm_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'АРМ добавлено'

            return HttpResponseRedirect(reverse('add_item', args=(item,)))
        else:
            request.session['status'] = 'danger'
            request.session['msg'] = form.errors
        return render(request, 'add_item.html', context=context)



class ShowItems(View):
    def _clear(self, lst):
        for i in range(len(lst)):
            if lst[i] == None or lst[i] == '':
                lst[i] = '-'
        return lst


    def get(self, request, items):
        context = {}
        if items == 'units':
            all_items = Unit.objects.all()
            if all_items:
                # pk, model, memory, os, id_naumen, id_invent, id_sn, arm, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.memory,
                     x.os,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Unit._meta._get_fields()[1:]]
                context.update({'title': 'Системные блоки', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Системные блоки" пуст.'})

        if items == 'monitors':
            all_items = Monitor.objects.all()
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Monitor._meta._get_fields()[1:]]
                context.update({'title': 'Мониторы', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Мониторы" пуст.'})

        if items == 'printers':
            all_items = Printer.objects.all()
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, ip, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.ip,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Printer._meta._get_fields()[1:]]
                context.update({'title': 'Принтеры', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Принтеры" пуст.'})

        if items == 'scanners':
            all_items = Scanner.objects.all()
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, id_sn_base, arm, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.id_sn_base,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Scanner._meta._get_fields()[1:]]
                context.update({'title': 'Сканеры', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Сканеры" пуст.'})

        if items == 'ibps':
            all_items = IBP.objects.all()
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in IBP._meta._get_fields()[1:]]
                context.update({'title': 'ИБП', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "ИБП" пуст.'})

        if items == 'phones':
            all_items = Phone.objects.all()
            if all_items:
                # pk, model, id_invent, id_sn, arm, ip, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.ip,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Phone._meta._get_fields()[1:]]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Телефоны" пуст.'})

        if items == 'routers':
            all_items = Router.objects.all()
            if all_items:
                # pk, model, id_invent, id_sn, ip, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_invent,
                     x.id_sn,
                     x.ip,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Router._meta._get_fields()]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Маршрутизаторы / свичи" пуст.'})

        if items == 'scales':
            all_items = Scale.objects.all()
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [self._clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Scale._meta._get_fields()[1:]]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Весы" пуст.'})

        return render(request, 'show_items.html', context=context)
