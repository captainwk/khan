from django.urls import path
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from instagram.views import FeedList
from instagram.views import UploadFeed

urlpatterns = [
    path('feed/', FeedList.as_view()),
    path('feed/upload/', UploadFeed.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
