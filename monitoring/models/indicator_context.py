from django.db import models
from django.contrib import admin


class IndicatorContextAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {'fields': ('name',)}),)


class IndicatorContext(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
