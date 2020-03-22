from django.db import models
from django.contrib import admin


class IndicatorCompositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {'fields': ('name',)}),)


class IndicatorComposition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
