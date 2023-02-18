from django.shortcuts import render
from .models import Video
from django.db.models import Q
from taggit.models import Tag
import requests


# Create your views here.


def search(request):
    results = []
    video_list = Video.objects.all().order_by('-id')
    tags = Tag.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if Video.objects.filter(Q(tags__name=query)):
                results = Video.objects.filter(Q(tags__name=query))
            else:
                results = Video.objects.filter(Q(title__icontains=query) |
                                               Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Video.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'video_list.html', {'videos': results, 'tags': tags})


def video_list(request):
    videos = Video.objects.filter(is_active=True)
    tags = Tag.objects.all()
    context = {'videos': videos, 'tags':tags}
    return render(request, 'video_list.html', context)


def video_details(request, v_id):
    url = "https://www.googleapis.com/youtube/v3/search?channelId=UCRy8zgRa5eyxWXTGZECQviw&videoEmbeddable=true&key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&q=&type=video"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    video = Video.objects.filter(pk=v_id)[0]
    context = {"video": video}
    return render(request, "video_details.html", context)
