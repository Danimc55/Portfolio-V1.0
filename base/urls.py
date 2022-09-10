from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.page, name="page"),
    path('contact', views.contact, name="contact")
]

