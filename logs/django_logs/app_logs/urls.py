from django.urls import path
from .views import first, second, third, four

urlpatterns = [
    path('1/', first),
    path('2/', second),
    path('3/', third),
    path('4/', four)
]
