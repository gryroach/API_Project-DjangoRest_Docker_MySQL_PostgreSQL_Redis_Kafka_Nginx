from django.urls import path
from .views import mirror_text, SinchPostView, SincView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', SinchPostView.as_view()),
    path('sinc', SincView.as_view())
]
