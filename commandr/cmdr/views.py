from django.shortcuts import render

from django.views.generic import ListView

from .models import cmdr


class Homepageview(ListView):
    model = cmdr
    template_name = 'home.html'
