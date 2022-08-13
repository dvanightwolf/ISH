from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.video_list, name='video_list'),

]
