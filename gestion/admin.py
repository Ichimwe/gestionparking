from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Parking)
admin.site.register(Reservation)
admin.site.register(Vehicle)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(Client)