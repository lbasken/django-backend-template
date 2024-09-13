from django.urls import path
from . import views


urlpatterns = [
    path('item/', views.get_all_items, name='get_all_items'),
]
