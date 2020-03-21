from django.db import models
from django.contrib import admin


class ScaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit',)
    fieldsets = ((None, {'fields': ('name', 'unit',)}),)


class Scale(models.Model):
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
