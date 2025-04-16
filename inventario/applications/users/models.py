from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ("admin", "Administrador"),
        ("user", "Usuario")
    ]

    username = models.CharField(verbose_name="Username", max_length=20, unique=True)
    email = models.EmailField(verbose_name="Email")
    nombres = models.CharField(verbose_name="Nombres", max_length=50, blank=True)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=50, blank=True)
    role = models.CharField(verbose_name="Rol", choices=ROLE_CHOICES, max_length=20, default="admin")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role"]

    objects = UserManager()
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"