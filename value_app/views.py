from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from value_app.models import Value
from django.views.generic.list import ListView
from value_app.forms import CreateValueForm
import requests
import random 
import json
from django.http import HttpResponseRedirect
          

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
      # #Using dictionary notation, get the 'results' field of the JSON,
      # # which contains the GIFs as a list, 
      # # If statement checks to make sure that if the server doesnt have anything to return, it doesnt crash
      # if response.status_code == 200:
      #     nonprof_list = nonprof_json['results']
      # else:
      #     gif_list = None
      #print(nonprof_list)
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict})




        





      
