from django.shortcuts import render
from .models import Audio, AudioTag
from django.db.models import Q

# Create your views here.


def search(request):
    results = []
    audio_list = Audio.objects.all().order_by('-id')
    tags = AudioTag.objects.all()
    tag = AudioTag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = AudioTag.objects.filter(pk=tag_id)
        if query != '':
            if Audio.objects.filter(Q(tags__name=query)):
                results = Audio.objects.filter(Q(tags__name=query))
            else:
                results = Audio.objects.filter(Q(title__icontains=query) |
                                               Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Audio.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'audio_list.html', {'audios': results, 'tags': tags})


def audio_list(request):
    audios = Audio.objects.filter(is_active=True)
    tags = AudioTag.objects.all()
    context = {'audios': audios, 'tags': tags}
    return render(request, 'audio_list.html', context)


def audio_details(request, a_id):
    audio = Audio.objects.filter(pk=a_id)[0]
    context = {"audio": audio}
    return render(request, "audio_details.html", context)
