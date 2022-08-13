from django.shortcuts import render
from .models import Video
# Create your views here.


def video_list(request):
    videos = Video.objects.filter(is_active=True)
    context = {'videos': videos}
    return render(request, 'video_list.html', context)
