from django.urls import path

from . import views

urlpatterns = [
    path("", views.redemption_model, name='redemption_model')
]