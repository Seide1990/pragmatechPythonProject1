

from django import urls
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
#from index.views import Home

from mekteb import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mekteb/',views.siyahi,name='mekteb'),
    path('',views.index,name='index'),

    
]

