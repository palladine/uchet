from django.contrib import admin
from .models import User, Unit, Monitor, Printer, Scanner, IBP, Scale, Phone, Router, ARM

class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email', 'role']
admin.site.register(User, UserAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'memory', 'os', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'retired']
admin.site.register(Unit, UnitAdmin)


class MonitorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'retired']
admin.site.register(Monitor, MonitorAdmin)


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'ip', 'retired']
admin.site.register(Printer, PrinterAdmin)


class ScannerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_naumen', 'id_invent', 'id_sn', 'id_sn_base', 'arm', 'retired']
admin.site.register(Scanner, ScannerAdmin)


class IBPAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'retired']
admin.site.register(IBP, IBPAdmin)


class ScaleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'retired']
admin.site.register(Scale, ScaleAdmin)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_invent', 'id_sn', 'arm', 'ip', 'retired']
admin.site.register(Phone, PhoneAdmin)


class RouterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'id_invent', 'id_sn', 'ip', 'retired']
admin.site.register(Router, RouterAdmin)

class ARMAdmin(admin.ModelAdmin):
    list_display = ['pk', 'unit_arm', 'monitor_arm']
admin.site.register(ARM, ARMAdmin)
