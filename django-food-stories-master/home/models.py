from django.db import models

# Create your models here.
class About(models.Model):
    image=models.ImageField(upload_to='about/',null=True, blank=True)
    slogan=models.TextField(default='Far far away, behind the word mountains, far from the countries Vokalia and Consonantia')
    daily_visitor=models.IntegerField(default=10)
    adress=models.TextField(help_text="enter company's current adress")
    phone=models.CharField(max_length=155,default='+2 392 3929 210')
    email=models.CharField(max_length=123,default='	info@yourdomain.com')
    twitter=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    instagram=models.URLField(null=True,blank=True)
    
    def __str__(self):
        return 'about'