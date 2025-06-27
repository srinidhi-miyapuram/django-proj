from django.db import models

# Create your models here.
class UserDetails(models.Model):
    
    firstName = models.CharField(max_length=264, default="test")
    lastName = models.CharField(max_length=264, default="test")
    email = models.EmailField(max_length=265, unique=True, default="test@gmail.com")
    
    def __str__(self):
        return self.firstName

