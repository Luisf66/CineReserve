from django.contrib import admin
from .models import Ticket


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ('reservation', 'created_at')

admin.site.register(Ticket, TicketAdmin)
