from django.urls import path
from .views import recipes


app_name='recipes'

urlpatterns = [
    path('', recipes, name='recipes'),
]