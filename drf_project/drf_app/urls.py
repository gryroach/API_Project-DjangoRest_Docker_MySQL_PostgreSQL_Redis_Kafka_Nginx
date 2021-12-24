from django.urls import path
from .views import mirror_text

urlpatterns = [
    path('', mirror_text)
]
