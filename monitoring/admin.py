from django.contrib import admin
from monitoring.models import context


admin.site.register(context.Context, context.ContextAdmin)