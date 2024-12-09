from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.leaderboard, name='leaderboard'),  # GET
    path('submit-score/', views.submit_score, name='submit_score'),  # POST
]
