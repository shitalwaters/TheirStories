from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("resources/", views.resources, name="resources"),
    path("mentor/<str:mentor_name>", views.detail, name="detail"),
]