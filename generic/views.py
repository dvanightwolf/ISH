import requests
from apscheduler.schedulers.background import BackgroundScheduler
from video.models import Video
from .models import Category
from django.utils.text import slugify
from taggit.models import Tag
from django.shortcuts import render


# Create your views here.
def youtube_api():
    """page_token = "CAoQAA"

    url = f"https://www.googleapis.com/youtube/v3/search?" \
          f"channelId=UCRy8zgRa5eyxWXTGZECQviw&videoEmbeddable=true&" \
          f"key=AIzaSyC6oTBsOzfiJ5zcue5PTb8VJZvgT_Wd_KU&part=snippet&" \
          f"type=video&maxResults=10&pageToken={page_token}"

    response = requests.request("GET", url)
    response = response.json()
    items = response["items"]
    for item in items:
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]
        title = snippet["title"]
        description = snippet["description"]
        thumbnail = snippet["thumbnails"]["high"]["url"]
        video = Video()
        tags = Tag()
        if not Video.objects.filter(video_id=video_id):
            if not Tag.objects.filter(name="lfvlfvkl"):
                tags = Tag.objects.create(name="lfvlfvkl", slug=slugify("lfvlfvkl"))
            video = Video.objects.create(video_id=video_id, title=title, thumbnail=thumbnail,
                                         category=Category.objects.first(), description=description,
                                         video_date="2021-02-02", slug=slugify(title),
                                         tags=tags)
            print(video.tags)"""
    video = Video.objects.create(video_id="video_id", title="title", thumbnail="https://thumbnail",
                                 category=Category.objects.first(), description="description",
                                 video_date="2021-02-02", slug=slugify("title"),
                                 tags=Tag.objects.filter(name="asd"))

    video.save()

    print(Video.objects.first().tags)


def scheduler():
    sch = BackgroundScheduler()
    sch.add_job(youtube_api, 'interval', seconds=1)
    sch.start()
