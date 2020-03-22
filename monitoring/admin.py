from django.contrib import admin
from monitoring.models import indicator, indicator_composed, indicator_composition, indicator_context, measurement, \
    scale, unit, unit_conversion


admin.site.register(indicator.Indicator, indicator.IndicatorAdmin)
admin.site.register(indicator_composed.IndicatorComposed, indicator_composed.IndicatorComposedAdmin)
admin.site.register(indicator_composition.IndicatorComposition, indicator_composition.IndicatorCompositionAdmin)
admin.site.register(indicator_context.IndicatorContext, indicator_context.IndicatorContextAdmin)
admin.site.register(measurement.Measurement, measurement.MeasurementAdmin)
admin.site.register(scale.Scale, scale.ScaleAdmin)
admin.site.register(unit.Unit, unit.UnitAdmin)
admin.site.register(unit_conversion.UnitConversion, unit_conversion.UnitConversionAdmin)
