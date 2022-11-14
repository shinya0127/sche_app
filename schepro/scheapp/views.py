from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from scheapp.models import Sche

# Create your views here.

class ScheList(ListView):
    model = Sche
    context_object_name = "schedules"

class ScheDetail(DetailView):
    model = Sche
    context_object_name = "schedule"

class ScheCreate(CreateView):
    model = Sche
    fields = "__all__"
    success_url = reverse_lazy("schedules")

class ScheUpdate(UpdateView):
    model = Sche
    fields = "__all__"
    success_url = reverse_lazy("schedules")

class ScheDelete(DeleteView):
    model = Sche
    fields = "__all__"
    success_url= reverse_lazy("schedule")
    context_object_name = "schedule"

