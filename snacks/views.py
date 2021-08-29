from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack

class SnackListView(ListView):
  model = Snack
  template_name = 'snack_list.html'

class SnackDetailView(DetailView):
  model = Snack
  template_name = 'snack_detail.html'

class SnackCreateView(CreateView):
  model = Snack
  template_name = 'snack_create.html'
  fields = ['name', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
  model = Snack
  template_name = 'snack_update.html'
  fields = ['name', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
  model = Snack
  template_name = 'snack_delete.html'
  success_url = reverse_lazy('snack_list') #Stack overflow helped me to figure out the reverse_lazy for the redirect 