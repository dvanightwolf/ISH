from django.urls import path
from . import views

app_name = "video"

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('search/', views.search, name='search'),
    path('details/<int:a_id>/', views.article_details, name='article_details'),

]
