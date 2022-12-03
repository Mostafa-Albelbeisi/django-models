from django.urls import path
from .views import HomePage, SnackListView, SnackDetail

urlpatterns=[
    path('',HomePage.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks' ),
    path('snacks/<int:pk>',SnackDetail.as_view(), name='detail')

]