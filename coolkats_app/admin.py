from django.contrib import admin
from .models import Mentor, AvailableTime
# Register your models here.
class MentorAdmin(admin.ModelAdmin):
    list_display=('id','name', 'fields', 'motivations')

class AvailableTimeAdmin(admin.ModelAdmin):
    list_display=('id', 'mentor', 'user', 'startTime')

admin.site.register(Mentor, MentorAdmin)
admin.site.register(AvailableTime, AvailableTimeAdmin)