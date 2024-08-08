from django.urls import path
from .views import homePageView, createView, removeView, listView, addItemView, removeItemView

urlpatterns = [
    path('', homePageView, name='home'),
    path('create/', createView, name='create'),
    path('remove/', removeView, name='remove'),
    path('list/<int:list_id>/', listView, name='list'),
    path('list/<int:list_id>/add/', addItemView, name='add-item'),
    path('list/<int:list_id>/remove/<int:item_id>/', removeItemView, name='remove-item'),
]
