from django.urls import path

from leaderboard.views import LeaderboardAPIView, SubmitScoreAPIView

urlpatterns = [
    path('top-score/', LeaderboardAPIView.as_view(), name='top_score'),  # GET
    path('submit-score/', SubmitScoreAPIView.as_view(), name='submit_score'),  # POST
]