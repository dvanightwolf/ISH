from django.shortcuts import render
from .models import Article, ArticleTag
from generic.models import Category
from django.db.models import Q


# Create your views here.


def search(request):
    results = []
    tags = ArticleTag.objects.all()
    tag = ArticleTag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = ArticleTag.objects.filter(pk=tag_id)
        if query != '':
            if Article.objects.filter(Q(articletag__tag__name=query)):
                results = Article.objects.filter(Q(tags__name=query))
            else:
                results = Article.objects.filter(Q(title__icontains=query) |
                                               Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Article.objects.all()

        if tag_id != '0':
            results = results.filter(Q(articletag__tag__name=tag[0].name))
    categories = Category.objects.all()
    context = {"articles": results, 'categories': categories, 'tags': tags}
    return render(request, 'article_list.html', context)


def article_list(request):
    articles = Article.objects.all()
    tags = []
    for tag in ArticleTag.objects.all():
        tags.append(tag.tag)
    categories = Category.objects.all()
    context = {'articles': articles, 'tags': tags, 'categories': categories}
    return render(request, 'article_list.html', context)


def article_details(request, v_id):
    article = Article.objects.filter(pk=v_id)[0]
    categories = Category.objects.all()
    context = {"article": article, 'categories': categories}
    return render(request, "article_details.html", context)
