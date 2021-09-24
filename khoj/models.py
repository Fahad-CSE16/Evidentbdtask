from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Results(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='results')
    input_values = ArrayField(models.IntegerField() ,blank=True, null=True)
    search_value = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)