from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Value
from django.views.generic.list import ListView


class LandingView(CreateView):
    """ Class to render landingpage. """

    def get(self, request):
        """ returns landing page. """
        return render(request, 'landingpage.html')

class DashboardView(CreateView):
    """ Class to render landingpage. """

    def get(self, request):
        """ returns landing page. """
        return render(request, 'dashboard.html')

class CreateValueView(ListView):
    """ Renders a list of all Pages. """
    model = Value

    def get(self, request):
        """ GET a list of Pages. """
        values = self.get_queryset().all()
        return render(request, 'create_value.html', {
          'values': values
        })
  