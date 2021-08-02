from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
from. import views


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('',ContactPageView.as_view(), name= 'contact' ),
]