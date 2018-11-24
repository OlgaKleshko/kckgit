from django.urls import path

from .views import AboutPageView, HomePageView, DetailPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('detail/', DetailPageView.as_view(), name='detail'),
]
