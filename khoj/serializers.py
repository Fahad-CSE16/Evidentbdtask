from django.contrib.postgres import fields
from django.db import models
from rest_framework import serializers
from .models import *

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['input_values','timestamp']
