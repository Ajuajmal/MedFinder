from django.urls import path

from . import views

urlpatterns = [
    path('', views.med_list, name="med_list"),
]
