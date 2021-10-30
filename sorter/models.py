from typing import List
from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class Sorter(models.Model):
    unsortedList = models.CharField(max_length=50,validators=[int_list_validator(sep=',', message=None, code='invalid', allow_negative=False)],default='3,1,2')

