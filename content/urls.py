from django.urls import path
from .views import ContentView, SendEmailView

urlpatterns = [
    path('content/', ContentView.as_view(), name='content'),
    path('send/', SendEmailView.as_view(), name='send'),
]
