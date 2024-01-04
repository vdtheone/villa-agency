from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("properties", views.properties, name="properties"),
    path("property_details", views.property_details, name="property_details"),
    path("contact", views.contact, name="contact")
]   