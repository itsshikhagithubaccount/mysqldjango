from django.forms import ModelForm, Textarea
from django.db import models


# stdclass Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
# stdclass Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()


class Students(models.Model):
    sId = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.EmailField(max_length=100)
    email = models.CharField(max_length=15)
class Meta:
    db_table ="stdclass"



