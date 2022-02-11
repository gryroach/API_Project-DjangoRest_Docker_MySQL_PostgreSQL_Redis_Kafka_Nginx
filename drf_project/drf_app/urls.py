from django.urls import path
from .views import mirror_text, SyncPostView, SyncAuthorView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', SyncPostView.as_view()),
    path('author/sync', SyncAuthorView.as_view()),
]
