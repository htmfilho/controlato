from django.db import models
from django.contrib import admin


class ContextAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {'fields': ('name',)}),)


class Context(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
