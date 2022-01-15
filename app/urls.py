from django.urls import path, include
# from django.conf.urls import url
from .views import UUIDgenApiView

urlpatterns = [
    path('', UUIDgenApiView.as_view()),
]