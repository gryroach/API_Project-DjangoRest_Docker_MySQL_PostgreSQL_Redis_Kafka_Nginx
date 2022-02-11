from django.urls import path
from .views import mirror_text, SinchPostView, SinchAuthorView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', SinchPostView.as_view()),
    path('author/sync', SinchAuthorView.as_view()),
]
