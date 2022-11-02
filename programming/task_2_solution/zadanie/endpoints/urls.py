from django.urls import path
from .views import EchoView, StatusView

urlpatterns = [
    path('echo/', EchoView.as_view()),
    path('status/', StatusView.as_view()),
]