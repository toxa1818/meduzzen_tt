from django.shortcuts import render
from django.urls import reverse
from .models import Worker, Service


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
