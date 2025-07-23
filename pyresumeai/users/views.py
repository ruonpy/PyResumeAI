from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Custom Login
class Login(LoginView):
    template_name="auth/login.html"
    redirect_authenticated_user=True

# Custom SignUp
class SignUp(CreateView):
    template_name="auth/signup.html"

# Custom Logout
class Logout(LogoutView):
    next_page=reverse_lazy("/")
    