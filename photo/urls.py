from django.urls import path
from . import views

app_name = "photo"

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('search/', views.search, name='search'),
    path('details/<int:p_id>/', views.photo_details, name='photo_details'),

]
