from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from value_app.models import Value
from django.views.generic.list import ListView
from value_app.forms import CreateValueForm
import requests
import random 
import json
from django.http import HttpResponseRedirect
from value_app.forms import CreateValueForm        
from django.views.generic.detail import DetailView

class LandingView(CreateView):
    """ Class to render landingpage. """

    def get(self, request):
        """ returns landing page. """
        return render(request, 'landingpage.html')



class DashboardView(ListView):
    """ Renders a list of all Pages. """
    model = Value

    def get(self, request):
        """ GET a list of Pages. """
        values = self.get_queryset().all()
        return render(request, 'dashboard.html', {
          'values': values
        })
  
class NonprofList(CreateView):
    """ Class to render landingpage. """
    def get(self, request):
      # stores params in a dict variable for the api respponse
      user_search = request.GET.get("search")
      params = {
      "q": user_search,
      }

      #retrieves the API response 
      response = requests.get("https://projects.propublica.org/nonprofits/api/v2/search.json?", params)
      # stores the api response in json in a dict variable
      # print(response)
      nonprof_json = response.json()
      # print(nonprof_json)

      orgs_list_dict = nonprof_json['organizations']
      form = CreateValueForm
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict,'form': form})
    
    def post(self, request, *args, **kwargs):
      form = CreateValueForm(request.POST)
      if form.is_valid():
          value = form.save()
          return HttpResponseRedirect(reverse_lazy('dashboard'))
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict,'form': form})


class ValueUpdateView(UpdateView):
    model = Value
    template_name = 'nonprof_list.html'
    form_class = CreateValueForm
    success_url = '/dashboard'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Value, slug=slug)

    # def post(self, request, *args, **kwargs):
    #   form = CreateValueForm(request.POST)
    #   if form.is_valid():
    #       value = form.save()
    #       return HttpResponseRedirect(reverse_lazy('dashboard'))
    #   return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict,'form': form})

class NonprofDetailView(DetailView):
    model = Value
    template_name = 'nonprof_detail.html'

    def get_queryset(self):
        return Value.objects.filter()

    # def get(self, request):
    #     user_search = get_object_or_404(self.model, pk=_pk)
    #     # stores params in a dict variable for the api respponse
    #     params = {
    #     "q": user_search,
    #     }

    #     #retrieves the API response 
    #     response = requests.get("https://projects.propublica.org/nonprofits/api/v2/search.json?", params)
    #     # stores the api response in json in a dict variable
    #     # print(response)
    #     nonprof_json = response.json()
    #     # print(nonprof_json)

    #     orgs_list_dict = nonprof_json['organizations']
    #     # form = CreateValueForm
    #     return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict})


