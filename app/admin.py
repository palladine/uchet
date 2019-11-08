from django.contrib import admin
from .models import User, Unit

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email', 'role']

admin.site.register(User, UserAdmin)



class UnitAdmin(admin.ModelAdmin):
    list_display = ['pk', 'model', 'memory', 'os', 'id_naumen', 'id_invent', 'id_sn', 'arm', 'retired']

admin.site.register(Unit, UnitAdmin)