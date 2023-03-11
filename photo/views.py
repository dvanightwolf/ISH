from django.shortcuts import render
from .models import Photo
from django.db.models import Q
from generic.models import Tag

# Create your views here.


def search(request):
    results = []
    photo_list = Photo.objects.all().order_by('-id')
    tags = Tag.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if Photo.objects.filter(Q(tags__name=query)):
                results = Photo.objects.filter(Q(tags__name=query))
            else:
                results = Photo.objects.filter(Q(title__icontains=query) |
                                               Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Photo.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'photo_list.html', {'photos': results, 'tags': tags})


def photo_list(request):
    photos = Photo.objects.filter(is_active=True)
    tags = Tag.objects.all()
    context = {'photos': photos, 'tags': tags}
    return render(request, 'photo_list.html', context)


def photo_details(request, p_id):
    photo = Photo.objects.filter(pk=p_id)[0]
    context = {"photo": photo}
    return render(request, "photo_details.html", context)
