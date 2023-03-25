import requests
from apscheduler.schedulers.background import BackgroundScheduler
from audio.models import Audio
from video.models import Video, VideoTag
from photo.models import Photo
from .models import Category
from .models import Tag, Category, Channel
from django.shortcuts import render


# Create your views here.
def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


def playlists():
    url = f"https://www.googleapis.com/youtube/v3/playlists?" \
          f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&channelId={Channel.objects.first().ch_id}&part=snippet"

    response = requests.request("GET", url)
    categories = response.json()["items"]
    new_categories = []
    page_token = ""
    try:
        while True:
            for cat in categories:
                if not Category.objects.filter(cat_id=cat["id"]):
                    Category.objects.create(name=cat["snippet"]["title"],
                                            cat_id=cat["id"],
                                            slug=slugify(cat["snippet"]["title"]), cat_type='YouTube')
                new_categories.append(cat["id"])

            page_token = response.json()["nextPageToken"]
            url = f"https://www.googleapis.com/youtube/v3/playlists?" \
                  f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU" \
                  f"&channelId={Channel.objects.first().ch_id}&part=snippet&pageToken={page_token}&maxResults=50"
            response = requests.request("GET", url)
            categories = response.json()["items"]

    except:
        for cat in categories:
            if not Category.objects.filter(cat_id=cat["id"]):
                Category.objects.create(name=cat["snippet"]["title"],
                                        cat_id=cat["id"],
                                        slug=slugify(cat["snippet"]["title"]), cat_type='YouTube')
            new_categories.append(cat["id"])

    finally:
        for category in Category.objects.filter(cat_type='YouTube'):
            can_delete = True
            for cat in new_categories:
                if category.cat_id == cat:
                    can_delete = False
            if can_delete:
                category.delete()


def playlist_items(cat_id):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?" \
          f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&" \
          f"playlistId={cat_id}&part=snippet&maxResults=50"
    response = requests.request("GET", url)
    page_token = ""
    playlists_items = []
    try:
        while True:
            playlists_items.extend(response.json()["items"])
            page_token = response.json()["nextPageToken"]
            url = f"https://www.googleapis.com/youtube/v3/playlistItems?" \
                  f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&" \
                  f"playlistId={cat_id}&part=snippet&maxResults=50&pageToken={page_token}"
            response = requests.request("GET", url)
    except:
        pass
    return playlists_items


def youtube_video_details():
    new_video_list = []
    for category in Category.objects.all():
        for item in playlist_items(cat_id=category.cat_id):
            video_id = item["snippet"]["resourceId"]["videoId"]
            url = f"https://www.googleapis.com/youtube/v3/videos?" \
                  f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&part=snippet&id={video_id}"
            response = requests.request("GET", url)
            video = response.json()["items"]
            if video:
                video = video[0]
                new_video = Video()
                new_video_list.append(video_id)
                thumbnail_url = ""
                for thumbnail in video["snippet"]["thumbnails"]:
                    thumbnail_url = video["snippet"]["thumbnails"][thumbnail]["url"]
                if not Video.objects.filter(video_id=video_id):
                    new_video = Video.objects.create(title=video["snippet"]["title"],
                                                     slug=slugify(video["snippet"]["title"]),
                                                     thumbnail=thumbnail_url, category=category,
                                                     description=video["snippet"]["description"],
                                                     video_id=video_id,
                                                     video_date="2002-02-02",)
                    new_video_list.append(new_video.video_id)
                    new_video.save()
                try:
                    tags = video["snippet"]["tags"]
                    new_tag = Tag()
                    for tag in tags:
                        if not Tag.objects.filter(name=tag):
                            new_tag = Tag.objects.create(name=tag, slug=slugify(tag))
                            new_tag.save()
                        VideoTag.objects.create(tag=new_tag, video=new_video)
                except:
                    pass
    return new_video_list


def youtube_api():
    playlists()
    new_video_list = youtube_video_details()
    for video in Video.objects.all():
        can_delete = True
        for new_video in new_video_list:
            if video.video_id == new_video:
                can_delete = False
        if can_delete:
            video.delete()


def scheduler():
    sch = BackgroundScheduler()
    sch.add_job(youtube_api, 'interval', hours=12)
    sch.start()


def base(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {'categories': categories, 'tags': tags}
    return render(request, "temp_home.html", context)
