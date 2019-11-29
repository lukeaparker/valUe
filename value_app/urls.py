from django.urls import path
from value_app.views import LandingView
from value_app.views import CreateValueView
from value_app.views import DashboardView
from value_app.views import Value
from . import views

urlpatterns = [
    path('', LandingView.as_view(), name='landingpage'),
    path('create_value/', CreateValueView.as_view(), name='create_value'),
    path('dashboard/', CreateValueView.as_view(), name='dashboard'),
]