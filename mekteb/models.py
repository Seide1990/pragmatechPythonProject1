from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Muellimler(models.Model):
    ad=models.CharField(max_length=127,null=True,blank=True)
    soyad=models.CharField(max_length=127,null=True,blank=True)
    tarix=models.DateTimeField(auto_now_add=True)
    fenn=models.ForeignKey('Fennler',on_delete=models.CASCADE,null=True, related_name='Fennlers')
    #image=models.ImageField(upload_to='media/product/images')

    def __str__(self):
         return self.ad        # admin sehifesinde titleler gorunsun
class Fennler(models.Model):
    fenn=models.CharField(max_length=127,null=True,blank=True)


    def __str__(self):
         return self.fenn        # admin sehifesinde titleler gorunsun

class sagirdler(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(sagirdler)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline