from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CarForm
from .models import Car
# Create your views here.

class CarList(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
class CreateCars(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create_cars.html'
    success_url = reverse_lazy('cars')