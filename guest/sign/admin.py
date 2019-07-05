'''
@Author: joker.zhang
@Date: 2019-06-28 13:59:05
@LastEditors: joker.zhang
@LastEditTime: 2019-07-04 17:37:52
@Description: For Automationr
'''
from django.contrib import admin
from sign.models import Event,Guest

#Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','sign','start_time','id']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)