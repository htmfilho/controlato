from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from monitoring.models import indicator_context, measurement


def index(request):
    indicator_contexts = indicator_context.IndicatorContext.objects.all()
    return render(request, "index.html", locals())


def context(request, context_id):
    ind_context = get_object_or_404(indicator_context.IndicatorContext, pk=context_id)
    return render(request, "context.html", locals())


def context_chart(request, context_id):
    ind_context = get_object_or_404( indicator_context.IndicatorContext, pk=context_id)
    measurements = measurement.Measurement.objects.filter(indicator_context=ind_context)

    labels = [m.measurement_date.strftime("%Y-%m-%d %H:%M:%S") for m in measurements]
    values = [m.value for m in measurements]

    chart = {'scale': ind_context.indicator.scale.name,
             'unit': ind_context.indicator.scale.unit.acronym,
             'chart': ind_context.chart,
             'labels': labels,
             'dataset': values}
    return JsonResponse(chart)
