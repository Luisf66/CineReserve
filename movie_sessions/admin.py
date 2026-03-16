from django.contrib import admin
from .models import Session

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    model = Session
    list_display = ('movie', 'start_time', 'room_number')

admin.site.register(Session, SessionAdmin)
