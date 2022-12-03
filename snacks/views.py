from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

class HomePage(TemplateView):
    template_name='home.html'

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetail(DetailView):
    template_name='snack_detail.html'
    model=Snack