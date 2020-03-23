from django.db import models
from django.contrib import admin


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    fieldsets = ((None, {'fields': ('name', 'acronym')}),)


class Unit(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
