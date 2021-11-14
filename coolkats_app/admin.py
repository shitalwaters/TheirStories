from django.contrib import admin
from .models import Mentor
# Register your models here.
class MentorAdmin(admin.ModelAdmin):
    list_display=('id','name', 'fields', 'motivations')

admin.site.register(Mentor)