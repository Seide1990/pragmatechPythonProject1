from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    mesage=models.TextField()
    subject=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
        
  
        
