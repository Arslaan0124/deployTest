from django.db import models
from django.core.validators import int_list_validator
# Create your models here.

class SortArray(models.Model):
    unsortedList = models.CharField(max_length=1000,validators=[int_list_validator(sep = ',')],default='1,2,3')
