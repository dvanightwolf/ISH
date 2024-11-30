# from django.shortcuts import render
# from .models import Audio, AudioTag
# from django.db.models import Q

# # Create your views here.


# def search(request):
#     results = []
#     audio_list = Audio.objects.all().order_by('-id')
#     tags = AudioTag.objects.all()
#     tag = AudioTag()
#     query = None
#     if request.method == 'GET':
#         query = request.GET.get('search')
#         tag_id = request.GET.get('tag', 'None')
#         if tag:
#             tag = AudioTag.objects.filter(pk=tag_id)
#         if query != '':
#             if Audio.objects.filter(Q(tags__name=query)):
#                 results = Audio.objects.filter(Q(tags__name=query))
#             else:
#                 results = Audio.objects.filter(Q(title__icontains=query) |
#                                                Q(description__icontains=query))
#         elif query == '' or tag == "0":
#             results = Audio.objects.all()

#         if tag_id != '0':
#             results = results.filter(Q(tags__name=tag[0].name))

#     return render(request, 'audio_list.html', {'audios': results, 'tags': tags})


# def audio_list(request):
#     audios = Audio.objects.filter(is_active=True)
#     tags = AudioTag.objects.all()
#     context = {'audios': audios, 'tags': tags}
#     return render(request, 'audio_list.html', context)


# def audio_details(request, a_id):
#     audio = Audio.objects.filter(pk=a_id)[0]
#     context = {"audio": audio}
#     return render(request, "audio_details.html", context)



from django.shortcuts import render
from .models import Audio, AudioTag
from django.db.models import Q

DEFAULT_TAG_ID = '0'

def filter_audios(query=None, tag_id=None):
    results = Audio.objects.all()
    if query:
        results = results.filter(Q(title__icontains=query) |
                                 Q(description__icontains=query) |
                                 Q(tags__name__icontains=query))
    if tag_id and tag_id != DEFAULT_TAG_ID:
        try:
            tag = AudioTag.objects.get(pk=tag_id)
            results = results.filter(tags__name=tag.name)
        except AudioTag.DoesNotExist:
            pass
    return results

def search(request):
    query = request.GET.get('search', '').strip()
    tag_id = request.GET.get('tag', DEFAULT_TAG_ID)
    results = filter_audios(query=query, tag_id=tag_id)
    tags = AudioTag.objects.all()
    return render(request, 'audio_list.html', {'audios': results, 'tags': tags})

def audio_list(request):
    audios = Audio.objects.filter(is_active=True)
    tags = AudioTag.objects.all()
    return render(request, 'audio_list.html', {'audios': audios, 'tags': tags})

def audio_details(request, a_id):
    try:
        audio = Audio.objects.get(pk=a_id)
    except Audio.DoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, "audio_details.html", {"audio": audio})

