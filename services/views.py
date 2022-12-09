from django.shortcuts import render
from .models import Worker, Service, Entries


def main(request):
    return render(request, 'services/main.html')

def workers(request):
    workers = Worker.objects.order_by('first_name')
    context = {'workers': workers}
    return render(request, 'services/workers.html', context)

def services(request):
    services = Service.objects.order_by('name')
    context = {'services': services}
    return render(request, 'services/services.html', context)

def entries(request):
    entries = Entries.objects.order_by('start_time')
    context = {'entries': entries}
    return render(request, 'services/timetable.html', context)

def show_one_entry(request, entry_id):
    entry = Entries.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'services/entry.html', context)
