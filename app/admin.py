from django.contrib import admin
from .models import User, Unit, Monitor, Printer, Scanner

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