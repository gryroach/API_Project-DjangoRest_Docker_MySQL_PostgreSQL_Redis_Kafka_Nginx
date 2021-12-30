from django.urls import path
from .views import mirror_text, SinchPostView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', SinchPostView.as_view())
]
