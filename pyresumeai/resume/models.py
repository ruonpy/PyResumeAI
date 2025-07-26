from django.db import models
from django.contrib.auth.models import User

class WorkExperience(models.model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_experiences")
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)
    currently_working=models.BooleanField(default=False)
    description=models.TextField(blank=True)
    def __str__(self):
        return f"{self.title} at {self.company}"
class Project(models.model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    name=models.CharField(max_length=200)
    tools_used=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField()
    url=models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name
    
