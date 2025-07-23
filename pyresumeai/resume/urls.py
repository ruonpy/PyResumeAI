from django.urls import path
from .views import Resume
urlpatterns=[
    path("", Resume.as_view(), name="resume")
]