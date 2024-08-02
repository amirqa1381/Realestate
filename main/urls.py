from django.urls import path
from .views import IndexView, AboutView, BlogListView, PropertyListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('properties/', PropertyListView.as_view(), name='properties'),
]
