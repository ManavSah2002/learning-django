from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path("", views.index, name='Home'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
]
