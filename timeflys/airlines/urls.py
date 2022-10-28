from django.urls import path
from airlines import views

urlpatterns = [
    path('', views.index)
]