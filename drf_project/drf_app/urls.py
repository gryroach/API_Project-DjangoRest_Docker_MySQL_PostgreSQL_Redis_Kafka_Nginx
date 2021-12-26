from django.urls import path
from .views import mirror_text, sinch_post

urlpatterns = [
    path('', mirror_text),
    path('post/sync', sinch_post)
]
