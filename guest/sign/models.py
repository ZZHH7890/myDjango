'''
@Author: joker.zhang
@Date: 2019-06-28 13:59:05
@LastEditors: joker.zhang
@LastEditTime: 2019-07-09 16:41:21
@Description: For Automation
'''
from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)
    events = models.Manager()

    def __str__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    guests = models.Manager()

    class Meta:
        unique_together = ('event','phone')

    def __str__(self):
        return self.realname