from django.contrib import admin
from monitoring.models import indicator_context, scale, unit, unit_conversion


admin.site.register(indicator_context.IndicatorContext, indicator_context.IndicatorContextAdmin)
admin.site.register(scale.Scale, scale.ScaleAdmin)
admin.site.register(unit.Unit, unit.UnitAdmin)
admin.site.register(unit_conversion.UnitConversion, unit_conversion.UnitConversionAdmin)
