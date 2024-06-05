from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/deribit', views.api_deribit, name='api_deribit'),
    path('chart/', views.chart_page, name='chart_page'),
]