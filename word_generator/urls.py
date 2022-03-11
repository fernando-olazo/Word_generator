from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # same thing as localhost:8000/
    path('random-word', views.r_word), #same thing as localhost:8000/random-word
    path('reset', views.reset) #same thing as localhost:8000/reset
]