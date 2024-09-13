from django.urls import path
from . import views


urlpatterns = [
    path('app/', views.list_apps, name='list_apps'),
]
