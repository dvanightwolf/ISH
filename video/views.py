from django.shortcuts import render
from .models import Video, VideoTag
from generic.models import Category
from django.db.models import Q


# Create your views here.


def search(request):
    results = []
    tags = VideoTag.objects.all()
    tag = VideoTag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = VideoTag.objects.filter(pk=tag_id)
        if query != '':
            if Video.objects.filter(Q(videotag__tag__name=query)):
                results = Video.objects.filter(Q(tags__name=query))
            else:
                results = Video.objects.filter(Q(title__icontains=query) |
                                               Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Video.objects.all()

        if tag_id != '0':
            results = results.filter(Q(videotag__tag__name=tag[0].name))
    categories = Category.objects.all()
    context = {"videos": results, 'categories': categories, 'tags': tags}
    return render(request, 'video_list.html', context)


def video_list(request):
    videos = Video.objects.all()
    tags = []
    for tag in VideoTag.objects.all():
        tags.append(tag.tag)
    categories = Category.objects.all()
    context = {'videos': videos, 'tags': tags, 'categories': categories}
    return render(request, 'video_list.html', context)


def video_details(request, v_id):
    video = Video.objects.filter(pk=v_id)[0]
    categories = Category.objects.all()
    context = {"video": video, 'categories': categories}
    return render(request, "video_details.html", context)
