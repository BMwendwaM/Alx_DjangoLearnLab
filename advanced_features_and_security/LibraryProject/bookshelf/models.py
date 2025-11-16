from django.contrib.auth.models import User, AbstractUser, UserManager

from django.db import models




# CustomeUser

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 

# Create book class.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} - {self.publication_year}"