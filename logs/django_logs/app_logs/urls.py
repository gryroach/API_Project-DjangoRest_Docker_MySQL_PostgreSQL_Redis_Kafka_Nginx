from django.urls import path
# from .views import first, second, third, four
from .views import first
urlpatterns = [
    path('1/', first)
]
