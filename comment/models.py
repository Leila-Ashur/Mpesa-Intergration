from django.db import models


# Create your models here.
class ReviewComments(models.Model):
    ratings = models.IntegerField()
    comments = models.TextField()
    equipment_name = models.CharField(max_length=32)
    Time_stamp = models.DateField()
    customer = models.CharField(max_length=32)

    def __str__(self):
        return f"Rating: {self.ratings}, Equipment: {self.equipment_name}"



