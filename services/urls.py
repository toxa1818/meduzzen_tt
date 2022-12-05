from django.urls import path
from . import views


app_name = 'services'
urlpatterns = [
    path('', views.main, name='main'),
    path('/services', views.services, name='services'),
    path('/workers', views.workers, name='workers'),
    #path('/timetable', views.timetable, name='timetable'),
]