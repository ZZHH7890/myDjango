'''
@Author: joker.zhang
@Date: 2019-06-28 13:59:05
@LastEditors: joker.zhang
@LastEditTime: 2019-07-08 18:19:02
@Description: For Automationr
'''
from django.contrib import admin
from sign.models import Event,Guest

#Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']
    search_fields = ['name']
    list_filter =['status']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname']
    list_filter =['sign']

admin.site.register(Event,EventAdmin)
#admin.site.register(Event)
admin.site.register(Guest,GuestAdmin)
#admin.site.register(Guest)