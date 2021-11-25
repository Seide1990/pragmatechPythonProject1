from django.urls import path
from stories import views


app_name='stories'

urlpatterns = [
    path('', views.stories, name='stories'),
    path('create_story/', views.create_story, name='create_story'),
    path('single/', views.single, name='single'),
    
]