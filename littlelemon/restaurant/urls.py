from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('', index, name='index'),
    path('menu/items', MenuItemView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
]