from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),   # Leaving the url blank, e.g. '', is a reference to the homepage
]
