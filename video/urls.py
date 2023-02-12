from django.urls import path
from . import views

app_name = "video"

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('search/', views.search, name='search'),
    path('details/<int:v_id>/', views.video_details, name='video_details'),

]
