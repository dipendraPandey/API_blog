from django.urls import path
 

 # importing the views here
from .views import home_screen_view
app_name = 'personal'
 
urlpatterns = [
    path('',home_screen_view, name='home'),
]