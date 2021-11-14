from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"), 
    path("logout/", views.logoutUser, name="logout"),
    path("resources/", views.resources, name="resources"),
    path("mentor/<int:mentor_id>", views.mentor, name="mentor"),
    path("booksession/<int:mentor_id>/<int:user_id>/<int:session_id>", views.bookSession, name="bookSession")
]