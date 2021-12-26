from django.urls import path
from .views import mirror_text, sinch_post, SinchPostView

urlpatterns = [
    path('', mirror_text),
    path('post/sync', sinch_post),
    path('post2/sync', SinchPostView.as_view())
]
