from django.db import models
from django.contrib import admin


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale',)
    fieldsets = ((None, {'fields': ('name', 'scale',)}),)


class Indicator(models.Model):
    scale = models.ForeignKey('Scale', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
