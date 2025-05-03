from django.urls import path
from . import views

urlpatterns = [
    path("", views.mail_sender, name="mail_sender"),
]
