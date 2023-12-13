from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('display_table', views.display_table, name='display_table'),
]