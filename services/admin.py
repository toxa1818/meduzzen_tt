from django.contrib import admin
from .models import Entries, Service, Worker, Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'car']


class EntriesAdmin(admin.ModelAdmin):
    list_display = ['client', 'start_time']


admin.site.register(Client, ClientAdmin)
admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Entries, EntriesAdmin)
