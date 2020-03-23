from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contexts/<int:context_id>/', views.context, name='context'),
    path('contexts/<int:context_id>/chart', views.context_chart),
]
