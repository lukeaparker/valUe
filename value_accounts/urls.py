from django.urls import path
from value_accounts.views import SignUpView


urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
]