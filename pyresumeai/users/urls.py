from django.urls import path
from .views import Login, SignUp, Logout
urlpatterns=[
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("register/", SignUp.as_view(), name="register"),
]