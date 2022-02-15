from django.urls import path
from .views import mirror_text, SyncPostView, SyncAuthorView, AuthorListView, AuthorDetailView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', SyncPostView.as_view()),
    path('author/sync', SyncAuthorView.as_view()),
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),
]
