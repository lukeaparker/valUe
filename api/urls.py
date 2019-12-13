from django.urls import path

from api.views import ValueList

urlpatterns = [
    path('value/', ValueList.as_view(), name='value_list'),
]
