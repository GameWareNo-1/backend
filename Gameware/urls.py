from django.contrib import admin
from django.urls import path, include
from level.views import LevelViewSet
level_list = LevelViewSet.as_view({'get': 'list', 'post': 'create'})
level_detail = LevelViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls.authtoken')),  # Optional: Token-based authentication
    path("custom-auth/", include("Auth.urls")),
    path('levels/', level_list, name='level-list'),
    path('levels/<int:pk>/', level_detail, name='level-detail'),
    path('game/', include('game.urls')),
    path("messages/", include("support.urls")),

]
