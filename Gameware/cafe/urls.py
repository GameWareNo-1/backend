from django.urls import path
from . import views
# URLConf
urlpatterns = [
    path('recipes/', views.Recipe_list),
    path('recipes/<int:id>/', views.Recipe_detail)
    
]
