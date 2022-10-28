from django.contrib import admin
from . import models

# Register your models here.


class LuggageAdmin(admin.ModelAdmin):
    list_display = ('name', 'airline', 'display_order', 'is_active')


class CancelationAdmin(admin.ModelAdmin):
    list_display = ('name', 'airline', 'display_order', 'is_active')



admin.site.register(models.Airline)
admin.site.register(models.LuggageRules, LuggageAdmin)
admin.site.register(models.CancelationRules, CancelationAdmin)