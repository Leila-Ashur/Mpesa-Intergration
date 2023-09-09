from django.db import models

# Create your models here.
class Comments (models.Model):
   ratings=models.IntegerField()
   comments=models.TextField()
   name=models.CharField(max_length=32)
   date=models.DateField()


    
def __str__(self) :
    return self.name
        
    

