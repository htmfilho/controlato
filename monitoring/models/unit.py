from django.db import models
from django.contrib import admin


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {'fields': ('name',)}),)


class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
