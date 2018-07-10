from django.shortcuts import render
from django.views import generic
from .models import Currency
from .scraper import *


class CurrencyListView(generic.list.ListView):
    def get_queryset(self):
        return Currency.objects.all()


class CurrentDetailView(generic.DetailView):
    def get_queryset(self):
        return Currency.objects.all()
