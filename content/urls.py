from django.urls import path
from content.views import IndexView, CreateNewPost


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("new", CreateNewPost.as_view(), name="new_post"),
]
