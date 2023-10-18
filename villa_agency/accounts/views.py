from django.shortcuts import render
from .models import Property

# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties':properties})


def contact(request):
    return render(request, 'contact.html')


def properties(request):
    return render(request, 'properties.html')


def property_details(request):
    return render(request, 'property_details.html')