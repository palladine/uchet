from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM
from django.views import View
from .forms import LoginForm, AddUnitForm, AddMonitorForm, AddPrinterForm, AddScannerForm, AddIBPForm, AddScaleForm, AddPhoneForm, AddRouterForm, AddARMForm
from django.urls import reverse
from django.db.models import Q
from barcode import generate
from uchet.settings import BASE_DIR, STATIC_URL

def _clear(lst):
    for i in range(len(lst)):
        if lst[i] == None or lst[i] == '':
            lst[i] = '-'
    return lst

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
            context = {'user': request.user, 'title': 'Главная', 'role': request.user.role}
            return render(request, 'home.html', context=context)
        else:
            return HttpResponseRedirect(reverse('login'))


class Search(View):
    def get(self, request):
        context = {}
        audit = request.GET.get('audit', '') == 'on'

        num = request.GET.get('search')

        if audit:
            arms_s = ARM.objects.filter(Q(barcode_id=num))
            printers_s = Printer.objects.filter(Q(barcode_id=num))
            ibps_s = IBP.objects.filter(Q(barcode_id=num))
            scanners_s = Scanner.objects.filter(Q(barcode_id=num))
            scales_s = Scale.objects.filter(Q(barcode_id=num))
            context.update({'arms': arms_s, 'printers': printers_s, 'ibps': ibps_s, 'scanners': scanners_s, 'scales': scales_s})
        else:
            arms_s = ARM.objects.filter(Q(pk=num) | Q(barcode_id=num))
            units_s = Unit.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num))
            monitors_s = Monitor.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num))
            printers_s = Printer.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num) | Q(barcode_id=num))
            ibps_s = IBP.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num) | Q(barcode_id=num))
            scanners_s = Scanner.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num) | Q(barcode_id=num))
            scales_s = Scale.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num) | Q(barcode_id=num))
            phones_s = Phone.objects.filter(Q(pk=num) | Q(id_naumen=num) | Q(id_invent=num) | Q(id_sn=num) | Q(barcode_id=num))
            routers_s = Router.objects.filter(Q(pk=num) | Q(id_invent=num) | Q(id_sn=num))

            context.update({'arms': arms_s, 'units': units_s, 'monitors': monitors_s, 'printers': printers_s,
                            'ibps': ibps_s, 'scanners': scanners_s, 'scales': scales_s, 'phones': phones_s,
                            'routers': routers_s})
        return render(request, 'search.html', context=context)



class AddItem(View):
    def get(self, request, item):
        if request.user.role == '1':
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
        else:
            return HttpResponseRedirect(reverse('home'))


    def _generate_barcode(self, id):
        len_id = len(str(id))
        cipher = 7
        zeros = cipher-len_id
        return ('0'*zeros)+str(id)

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

                # generate barcode
                printer_item.barcode_id = '{}{:0>7}'.format(ord('p'), printer_item.pk)
                printer_item.save()
                namecode = generate('code128', printer_item.barcode_id, output='{}/app{}codes/p/{}'.format(BASE_DIR, STATIC_URL, printer_item.barcode_id))

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


            # adding ARM
            # todo field scan-code to model + creating scan-code to arm!
            if item == 'arm':
                unit_arm_id = request.POST.get('unit_arm')
                monitor_arm_id = request.POST.get('monitor_arm')
                printer_arm_id = request.POST.get('printer_arm')
                scanner_arm_id = request.POST.get('scanner_arm')
                ibp_arm_id = request.POST.get('ibp_arm')
                scale_arm_id = request.POST.get('scale_arm')
                phone_arm_id = request.POST.get('phone_arm')
                comp_name_arm = request.POST.get('comp_name_arm')
                ip_arm = request.POST.get('ip_arm')
                comment_arm = request.POST.get('comment_arm')

                # creating new arm
                arm_item = ARM()

                ## required unit and monitor objects
                unit_obj = Unit.objects.get(pk=unit_arm_id)
                monitor_obj = Monitor.objects.get(pk=monitor_arm_id)

                arm_item.unit_arm = unit_obj
                arm_item.monitor_arm = monitor_obj

                arm_item.comp_name = comp_name_arm
                arm_item.ip = ip_arm
                arm_item.comment = comment_arm

                arm_item.save()

                # new arm object
                arm_obj = ARM.objects.get(pk=arm_item.pk)

                # adding new arm to unit
                unit_obj.arm = arm_obj
                unit_obj.save()

                # adding new arm to monitor
                monitor_obj.arm = arm_obj
                monitor_obj.save()

                if printer_arm_id:
                    printer_obj = Printer.objects.get(pk=printer_arm_id)
                    arm_item.printer_arm = printer_obj
                    printer_obj.arm = arm_obj
                    printer_obj.save()

                if scanner_arm_id:
                    scanner_obj = Scanner.objects.get(pk=scanner_arm_id)
                    arm_item.scanner_arm = scanner_obj
                    scanner_obj.arm = arm_obj
                    scanner_obj.save()

                if ibp_arm_id:
                    ibp_obj = IBP.objects.get(pk=ibp_arm_id)
                    arm_item.ibp_arm = ibp_obj
                    ibp_obj.arm = arm_obj
                    ibp_obj.save()

                if scale_arm_id:
                    scale_obj = Scale.objects.get(pk=scale_arm_id)
                    arm_item.scale_arm = scale_obj
                    scale_obj.arm = arm_obj
                    scale_obj.save()

                if phone_arm_id:
                    phone_obj = Phone.objects.get(pk=phone_arm_id)
                    arm_item.phone_arm = phone_obj
                    phone_obj.arm = arm_obj
                    phone_obj.save()

                arm_item.save()
                request.session['status'] = 'success'
                request.session['msg'] = 'АРМ добавлено'

            return HttpResponseRedirect(reverse('add_item', args=(item,)))
        else:
            request.session['status'] = 'danger'
            request.session['msg'] = form.errors
        return render(request, 'add_item.html', context=context)



class ShowItems(View):

    def get(self, request, items):
        context = {}
        if items == 'units':
            all_items = Unit.objects.all().order_by('-pk')
            if all_items:
                # pk, model, memory, os, id_naumen, id_invent, id_sn, arm, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.memory,
                     x.os,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Unit._meta.fields]
                context.update({'title': 'Системные блоки', 'heads': heads, 'vals': vals, 'item': 'unit'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Системные блоки" пуст.'})

        if items == 'monitors':
            all_items = Monitor.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Monitor._meta.fields]
                context.update({'title': 'Мониторы', 'heads': heads, 'vals': vals, 'item': 'monitor'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Мониторы" пуст.'})

        if items == 'printers':
            all_items = Printer.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, ip, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.ip,
                     x.barcode_id,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Printer._meta.fields]
                context.update({'title': 'Принтеры', 'heads': heads, 'vals': vals, 'item': 'printer'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Принтеры" пуст.'})

        if items == 'scanners':
            all_items = Scanner.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, id_sn_base, arm, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.id_sn_base,
                     x.arm,
                     x.barcode_id,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Scanner._meta.fields]
                context.update({'title': 'Сканеры', 'heads': heads, 'vals': vals, 'item': 'scanner'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Сканеры" пуст.'})

        if items == 'ibps':
            all_items = IBP.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.barcode_id,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in IBP._meta.fields]
                context.update({'title': 'ИБП', 'heads': heads, 'vals': vals, 'item': 'ibp'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "ИБП" пуст.'})

        if items == 'phones':
            all_items = Phone.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_invent, id_sn, arm, ip, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.ip,
                     x.barcode_id,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Phone._meta.fields]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals, 'item': 'phone'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Телефоны" пуст.'})

        if items == 'routers':
            all_items = Router.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_invent, id_sn, ip, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_invent,
                     x.id_sn,
                     x.ip,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Router._meta.fields]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals, 'item': 'router'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Маршрутизаторы / свичи" пуст.'})

        if items == 'scales':
            all_items = Scale.objects.all().order_by('-pk')
            if all_items:
                # pk, model, id_naumen, id_invent, id_sn, arm, retired
                vals = [_clear(
                    [x.pk,
                     x.model,
                     x.id_naumen,
                     x.id_invent,
                     x.id_sn,
                     x.arm,
                     x.barcode_id,
                     "Да" if x.retired else "Нет"]) for x in all_items]
                heads = [y.verbose_name for y in Scale._meta.fields]
                context.update({'title': 'Телефоны', 'heads': heads, 'vals': vals, 'item': 'scale'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "Весы" пуст.'})

        if items == 'arms':
            all_items = ARM.objects.all().order_by('-pk')
            if all_items:
                # pk, unit_arm, monitor_arm, printer_arm, scanner_arm, ibp_arm, scale_arm, phone_arm, comp_name, ip, comment
                vals = [_clear(
                    [x.pk,
                     x.unit_arm,
                     x.monitor_arm,
                     #x.printer_arm,
                     #x.scanner_arm,
                     #x.ibp_arm,
                     #x.scale_arm,
                     #x.phone_arm,
                     x.comp_name,
                     x.ip,
                     x.barcode_id,
                     x.comment
                     ]) for x in all_items]
                heads = [ARM._meta.get_field('id').verbose_name,
                         ARM._meta.get_field('unit_arm').verbose_name,
                         ARM._meta.get_field('monitor_arm').verbose_name,
                         ARM._meta.get_field('comp_name').verbose_name,
                         ARM._meta.get_field('ip').verbose_name,
                         ARM._meta.get_field('barcode_id').verbose_name,
                         ARM._meta.get_field('comment').verbose_name
                         ]
                context.update({'title': 'АРМы', 'heads': heads, 'vals': vals, 'item': 'arm'})
            else:
                context.update({'status': 'danger', 'msg': 'Список "АРМы" пуст.'})

        return render(request, 'show_items.html', context=context)


class CardItem(View):
    def get(self, request, item, id):

        context = {}

        if item == 'unit':
            rec = Unit.objects.get(pk=id)
            fields_rec = _clear([getattr(rec, i) if i != 'retired' else 'Нет' if getattr(rec, i) == False else 'Да' for i in [j.name for j in rec._meta.fields]])
            heads = [y.verbose_name for y in Unit._meta.fields]
            fields_list = list(zip(heads, fields_rec))
            context = {'fields': fields_list, 'title': 'Системный блок'}


        if item == 'monitor':
            rec = Monitor.objects.get(pk=id)
            fields_rec = _clear(
                [getattr(rec, i) if i != 'retired' else 'Нет' if getattr(rec, i) == False else 'Да' for i in [j.name for j in rec._meta.fields]])
            heads = [y.verbose_name for y in Monitor._meta.fields]
            fields_list = list(zip(heads, fields_rec))
            context = {'fields': fields_list, 'title': 'Монитор'}


        if item == 'printer':
            rec = Printer.objects.get(pk=id)
            fields_rec = _clear(
                [getattr(rec, i) if i != 'retired' else 'Нет' if getattr(rec, i) == False else 'Да' for i in [j.name for j in rec._meta.fields]])
            heads = [y.verbose_name for y in Printer._meta.fields]
            code = rec.barcode_id if rec.barcode_id else False
            fields_list = list(zip(heads, fields_rec))
            context = {'fields': fields_list, 'title': 'МФУ / Принтер', 'code': code, 'prefix': 'p'}


        return render(request, 'card_item.html', context=context)