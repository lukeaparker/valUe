from django.urls import path
from value_app.views import LandingView
from value_app.views import DashboardView
from value_app.views import Value
from value_app.views import NonprofList
from value_app.views import ValueUpdateView, NonprofDetailView

from . import views

urlpatterns = [
    path('', LandingView.as_view(), name='landingpage'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('nonprof_list/', NonprofList.as_view(), name='nonprof_list'),
    path('nonprof_list/<str:pk>/<str:slug>', NonprofDetailView.as_view(), name='nonprof_detail'),
    path('nonprof_list/<str:pk>/<str:slug>/update', ValueUpdateView.as_view(), name='nonprof_list_update')
]