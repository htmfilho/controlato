from django.db import models
from django.contrib import admin


class IndicatorComposedAdmin(admin.ModelAdmin):
    list_display = ('composition', 'indicator',)
    fieldsets = ((None, {'fields': ('composition', 'indicator',)}),)


class IndicatorComposed(models.Model):
    indicator = models.ForeignKey('Indicator', on_delete=models.CASCADE)
    composition = models.ForeignKey('IndicatorComposition', on_delete=models.CASCADE)
