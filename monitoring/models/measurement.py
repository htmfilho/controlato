from django.db import models
from django.contrib import admin


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('indicator_context', 'value', 'used_formula', 'filled_formula', 'measurement_date', 'record_date',)
    fieldsets = ((None, {'fields': ('indicator_context', 'value', 'used_formula', 'filled_formula', 'measurement_date',)}),)


class Measurement(models.Model):
    indicator_context = models.ForeignKey('IndicatorContext', on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=3, max_digits=12)
    used_formula = models.CharField(max_length=255, null=True, blank=True)
    filled_formula = models.CharField(max_length=255, null=True, blank=True)
    measurement_date = models.DateTimeField()
    record_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.value)
