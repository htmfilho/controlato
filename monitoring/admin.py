from django.contrib import admin
from monitoring.models import indicator_context


admin.site.register(indicator_context.IndicatorContext, indicator_context.IndicatorContextAdmin)