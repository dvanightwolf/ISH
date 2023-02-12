from django.urls import path
from . import views

app_name = "audio"

urlpatterns = [
    path('', views.audio_list, name='audio_list'),
    path('search/', views.search, name='search'),
    path('details/<int:a_id>/', views.audio_details, name='audio_details'),

]
