from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
        ('Custom','Custom')
    )
    phone=models.CharField(max_length=17, default='' ,blank=True, null=True)
    first_name=models.CharField(max_length=100, default='' ,blank=True, null=True)
    last_name=models.CharField(max_length=100, default='' ,blank=True, null=True)
    blood_group=models.CharField(max_length=10, default='' ,blank=True, null=True)
    date_of_birth=models.DateField(blank=True, null=True)
    gender=models.CharField( max_length=100, choices=CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True,)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','first_name','last_name','blood_group','date_of_birth','gender'] 
    objects = UserManager()

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

   