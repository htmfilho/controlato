from django.db import models
from django.contrib import admin


class UnitConversionAdmin(admin.ModelAdmin):
    list_display = ('unit_a', 'unit_b', 'formula',)
    fieldsets = ((None, {'fields': ('unit_a', 'unit_b', 'formula',)}),)


class UnitConversion(models.Model):
    unit_a = models.ForeignKey('Unit', on_delete=models.CASCADE)
    unit_b = models.ForeignKey('Unit', related_name='unit_b', on_delete=models.CASCADE)
    formula = models.CharField(max_length=100)

    def __str__(self):
        return self.formula
