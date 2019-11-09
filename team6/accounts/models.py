from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    email = models.TextField()
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username