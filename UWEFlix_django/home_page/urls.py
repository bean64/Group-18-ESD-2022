from django.urls import path
from home_page import views

urlpatterns = [
    path("", views.home, name="home"),
]