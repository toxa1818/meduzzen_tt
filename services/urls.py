from django.urls import path
from . import views


app_name = 'services'
urlpatterns = [
    path('', views.main, name='main'),
    path('/services', views.services, name='services'),
    path('/workers', views.workers, name='workers'),
    path('/timetable', views.entries, name='entries'),
    path('/timetable/<int:entry_id>', views.show_one_entry, name='entry')
]