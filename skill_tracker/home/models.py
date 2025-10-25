from django.db import models
from django.contrib.auth import get_user_model 
User = get_user_model()

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Checkpoint(models.Model):
    skill = models.ForeignKey(Skill, related_name='checkpoints', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name