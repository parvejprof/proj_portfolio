from django.urls import path
from . import views

urlpatterns = [
    path("", views.calc_index, name="calc_index"),
]
