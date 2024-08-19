from django.urls import path
from .views import (IndexView,
                    AboutView,
                    BlogListView,
                    PropertyListView,
                    SinglePropertyView,
                    PropertySellView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('properties/', PropertyListView.as_view(), name='properties'),
    path('single-property/<slug:slug>/', SinglePropertyView.as_view(), name='single-property'),
    path('property-sell/', PropertySellView.as_view(), name='property_sell'),
]
