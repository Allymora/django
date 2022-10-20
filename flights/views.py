from django.shortcuts import render 
from django.http import HttpResponse
from .models import Airport flights

# Create your views here.
def index(request):
    context{
        "flights" : Flights.objects.all()
    }
    return render(request, "flights/index.html")