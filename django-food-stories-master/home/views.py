from django.shortcuts import render
from .models import About
def index(request):
    return render(request, 'index.html')

def about(request):
    about1=About.objects.filter(pk=6).first
    content={'about':about1}
    return render(request, 'about.html')
