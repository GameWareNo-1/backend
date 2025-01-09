from django.urls import path
from . import views

urlpatterns = [
    path('top-score/', views.leaderboard, name='top_score'),  # GET
    path('submit-score/', views.submit_score, name='submit_score'),  # POST
]