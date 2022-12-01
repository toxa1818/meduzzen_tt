from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    car = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone_number} - {self.car}'


class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    experience = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.experience}years'


class Service(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.time}hours - {self.cost}$'


class Timetable(models.Model):
    start_time = models.DateTimeField(auto_now_add=False)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    list_of_services = models.ManyToManyField(Service)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
