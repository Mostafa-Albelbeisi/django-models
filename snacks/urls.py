from django.urls import path, include
from .views import Home, SnackDetail, SnackList, About

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("snackDetail", SnackDetail.as_view(), name="snackDetail"),
    path("snackList", SnackList.as_view(), name="snackList"),
    path("about", About.as_view(), name="about"),
]
