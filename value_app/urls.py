from django.urls import path
from value_app.views import LandingView
from value_app.views import DashboardView
from value_app.views import Value
from . import views

urlpatterns = [
    path('', LandingView.as_view(), name='landingpage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]