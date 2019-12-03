from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from value_app.models import Value
from django.views.generic.list import ListView
import random 
import json
from django.http import HttpResponseRedirect
from django.urls import reverse

from value_app.forms import CreateValueForm
          
    # If this is a GET (or any other method) create the default form.
    form = CreateValueForm(initial={'Value Tag': 'value tag'})
    context = {
        'form': form,
        'value_tag': 'value_tag',
    }

    return render(request, 'dashboard.html', context)


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

class DashboardView(ListView):
    """ Renders a list of all Pages. """
    model = Value

    def get(self, request):
        """ GET a list of Pages. """
        values = self.get_queryset().all()
        return render(request, 'dashboard.html', {
          'values': values
        })
  