from django.db import models
from django.contrib import admin


class IndicatorContextAdmin(admin.ModelAdmin):
    list_display = ('name', 'indicator',)
    fieldsets = ((None, {'fields': ('name', 'indicator',)}),)


class IndicatorContext(models.Model):
    indicator = models.ForeignKey('Indicator', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
