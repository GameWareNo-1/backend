from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateMessageView, ReplyMessageView,ListMessagesView
from . import views

urlpatterns = [
    path('create', CreateMessageView.as_view(), name='create-message'),
    path('', ListMessagesView.as_view(), name='list-message'),
    path('<int:pk>/', ReplyMessageView.as_view(), name='reply-message'),
]