from django.db import models
from django.contrib import admin


class IndicatorContextAdmin(admin.ModelAdmin):
    list_display = ('name', 'indicator', 'chart', 'interval')
    fieldsets = ((None, {'fields': ('name', 'indicator', 'chart', 'interval')}),)


CHART_LINE = 'line'
CHART_BAR = 'bar'
CHART_HORIZONTAL_BAR = 'horizontalBar'


CHART_CHOICES = ((CHART_LINE, "Line"),
                 (CHART_BAR, "Bar"),
                 (CHART_HORIZONTAL_BAR, "Horizontal Bar"))


INTERVAL_MILLISECOND = 'millisecond'
INTERVAL_SECOND = 'second'
INTERVAL_MINUTE = 'minute'
INTERVAL_HOUR = 'hour'
INTERVAL_DAY = 'day'
INTERVAL_WEEK = 'week'
INTERVAL_MONTH = 'month'
INTERVAL_QUARTER = 'quarter'
INTERVAL_YEAR = 'year'


INTERVAL_CHOICES = ((INTERVAL_MILLISECOND, 'Milliseconds'),
                    (INTERVAL_SECOND, 'Seconds'),
                    (INTERVAL_MINUTE, 'Minutes'),
                    (INTERVAL_HOUR, 'Hours'),
                    (INTERVAL_DAY, 'Days'),
                    (INTERVAL_WEEK, 'Weeks'),
                    (INTERVAL_MONTH, 'Months'),
                    (INTERVAL_QUARTER, 'Quarters'),
                    (INTERVAL_YEAR, 'Years'))


class IndicatorContext(models.Model):
    indicator = models.ForeignKey('Indicator', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    chart = models.CharField(max_length=20, choices=CHART_CHOICES, default=CHART_LINE)
    interval = models.CharField(max_length=20, choices=INTERVAL_CHOICES, default=INTERVAL_DAY)

    def __str__(self):
        return self.name
