from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateMessageView, ReplyMessageView
from . import views

urlpatterns = [
    path('messages/', CreateMessageView.as_view(), name='create-message'),
    path('messages/<int:pk>/', ReplyMessageView.as_view(), name='reply-message'),

]