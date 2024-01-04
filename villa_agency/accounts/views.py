from django.shortcuts import redirect, render
from .models import ContactUs, Property

# Create your views here.
def home(request):
    properties = Property.objects.all()[0:6]
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        detail = ContactUs(name=name, email=email, subject=subject, message=message)
        detail.save()
        redirect('/home')
    return render(request, 'home.html', {'properties':properties})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        detail = ContactUs(name=name, email=email, subject=subject, message=message)
        detail.save()
        redirect('/home')
    return render(request, 'contact.html')


def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties.html', {'properties':properties})


def property_details(request):
    return render(request, 'property_details.html')