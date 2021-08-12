from user import views
from django.urls import path

urlpatterns = [
    path('user', views.user, name='user'),
  
]