from django.urls import path
from .views import IndexView, AboutView, BlogListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
]
