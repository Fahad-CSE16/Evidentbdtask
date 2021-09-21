from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.
class Results(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='results')
    input_values=models.TextField()
    search_value=models.IntegerField()
    result=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)