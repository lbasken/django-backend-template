from django.urls import path
from . import views


urlpatterns = [
    path('item/', views.get_all_items, name='get_all_items'),
    path('item/new/', views.create_new_item, name='create_new_item'),
    path('item/<int:restaurant_id>/', views.get_item_by_id, name='get_item_by_id'),
    path('item/patch/<int:restaurant_id>/', views.update_item_by_id, name='update_item_by_id'),
    path('item/delete/<int:restaurant_id>/', views.delete_item_by_id, name='delete_item_by_id'),
]
