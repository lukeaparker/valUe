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
from value_app.forms import CreateValueForm        

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
<<<<<<< HEAD
      # #Using dictionary notation, get the 'results' field of the JSON,
      # # which contains the GIFs as a list, 
      # # If statement checks to make sure that if the server doesnt have anything to return, it doesnt crash
      # if response.status_code == 200:
      #     nonprof_list = nonprof_json['results']
      # else:
      #     gif_list = None
      #print(nonprof_list)
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict, "tag" : user_search})

    
    def get_tag(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CreateValueForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/dashboard/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CreateValueForm()
=======
      form = CreateValueForm
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict,'form': form})
    
    def post(self, request, *args, **kwargs):
      form = CreateValueForm(request.POST)
      if form.is_valid():
          value = form.save()
          return HttpResponseRedirect(reverse_lazy('dashboard'))
      return render(request, 'nonprof_list.html', {'nonprofs' : orgs_list_dict,'form': form})
>>>>>>> 6792fee23759700e99e193b87edcbaf6c42b7d23

        return render(request, 'dashboard.html', {'form': form})




            





          
