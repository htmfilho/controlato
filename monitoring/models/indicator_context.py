from django.db import models
from django.contrib import admin


class IndicatorContextAdmin(admin.ModelAdmin):
    list_display = ('name', 'indicator', 'chart')
    fieldsets = ((None, {'fields': ('name', 'indicator', 'chart')}),)


CHART_LINE = 'line'
CHART_BAR  = 'bar'
CHART_HORIZONTAL_BAR = 'horizontalBar'


CHART_CHOICES = ((CHART_LINE, "Line"),
                 (CHART_BAR, "Bar"),
                 (CHART_HORIZONTAL_BAR, "Horizontal Bar"))


class IndicatorContext(models.Model):
    indicator = models.ForeignKey('Indicator', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    chart = models.CharField(max_length=20, choices=CHART_CHOICES, default=CHART_LINE)

    def __str__(self):
        return self.name
