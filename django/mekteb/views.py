from django.http import request
from django.shortcuts import render

from mekteb.models import Muellimler

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def siyahi(request):
    
    return render(request,'mekteb.html')

def muellimler(request):
    muellim=Muellimler.objects.all   #databaseden datani secdik
 
    content={'muellim':muellim}
    return render(request,'muellimler.html',content)