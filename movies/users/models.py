from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, db_index=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUser(AbstractUser):
    create_date = models.DateTimeField(auto_now_add=True, db_index=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True



class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)



class User(BaseUser):
    
    username = models.CharField(_('Username of User'), max_length=999)
    first_name = models.CharField(_("First name of User"), max_length=999)
    last_name = models.CharField(_("Last name of User"), max_length=999)
    email = models.EmailField(
        _("email address"), unique=True, editable=True, max_length=999
    )
  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email


