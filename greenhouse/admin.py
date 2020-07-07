from django.contrib import admin
from .models import *


admin.site.register(AtmosphericPressure)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(SoilTemperature)
admin.site.register(SoilMoisture)
admin.site.register(Light)
admin.site.register(OutsideTemperature)
admin.site.register(HumidityOutside)
admin.site.register(ComfortIndicator)


# class ValueAdmin(admin.ModelAdmin):
#     list_filter = (
#         'graph',
#     )
#
#
# admin.site.register(Value, ValueAdmin)
