from django.db import models
from django.contrib import admin


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale', 'formula',)
    fieldsets = ((None, {'fields': ('name', 'scale', 'formula',)}),)


class Indicator(models.Model):
    scale = models.ForeignKey('Scale', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
