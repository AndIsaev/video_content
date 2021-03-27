from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from content import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("new", views.new_post, name="new_post"),
]