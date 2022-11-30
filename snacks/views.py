from django.shortcuts import render
from django .views.generic import TemplateView, ListView
from .models import Snack

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class SnackDetail(ListView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackList(ListView):
    template_name = 'snack_list.html'
    model = Snack


class About(TemplateView):
    template_name = 'about.html'