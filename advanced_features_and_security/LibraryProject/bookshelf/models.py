from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db import models





# CustomeUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username must be set")
        extra_fields.setdefault('date_of_birth', None)
        extra_fields.setdefault('profile_photo', None)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username=username, password=password, **extra_fields)

# CustomeUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 


# Create book class.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author} - {self.publication_year}"
    

# USER MODEL ROLE_BASED VIEWS
# Define roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookshelf_profile")
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.role}"