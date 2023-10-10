from django.contrib import admin

from .models import VWCar, ModelOfCar, DieselEngine

admin.site.register(VWCar)
admin.site.register(ModelOfCar)
admin.site.register(DieselEngine)