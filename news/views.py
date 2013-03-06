# Create your views here.
# from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from news.models import news_model
from djangomako.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown


def news_by_time_mako(request):
    contexts = {}
    news_list = news_model.objects.order_by('pub_time').filter(status='P').reverse()
    # news_list = range(18)
    paginator = Paginator(news_list, 8)
    page = request.GET.get('page')
    try:
        news_show = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_show = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_show = paginator.page(paginator.num_pages)
    contexts['news_list'] = news_show
    contexts['page'] = page
    return render_to_response('news/mako/news_time.html', {'contexts': contexts})


def news_by_cate_mako(request):
    contexts = {}
    cate = request.GET.get('cate')
    if not cate:
        cate = 'economy'
    news_list = news_model.objects.order_by('pub_time').filter(category=cate, status='P').reverse()
    # news_list = range(18)
    paginator = Paginator(news_list, 6)
    page = request.GET.get('page')
    try:
        news_show = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_show = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_show = paginator.page(paginator.num_pages)

    contexts['news_list'] = news_show
    contexts['page'] = page
    contexts['cate'] = cate
    return render_to_response('news/mako/news_cate.html', {'contexts': contexts})


def news_detail_mako(request, news_id):
    news_current = get_object_or_404(news_model, pk=news_id, status='P')
    html = markdown.markdown(news_current.article)
    news_current.article = html
    return render_to_response('news/mako/news_detail.html', {'news_current': news_current})


def news_like(request, news_id):
    news_current = get_object_or_404(news_model, pk=news_id, status='P')
    news_current.like += 1
    news_current.save()
    return render_to_response('news/mako/news_like.html', {})


def news_dislike(request, news_id):
    news_current = get_object_or_404(news_model, pk=news_id, status='P')
    news_current.dislike += 1
    news_current.save()
    return render_to_response('news/mako/news_like.html', {})


def news_by_time_bootstrap(request):
    news_list = []
    return render_to_response('news/bootstrap/news_time.html', {'news_list': news_list})


def news_by_cate_bootstrap(request):
    news_list = []
    return render_to_response('news/bootstrap/news_cate.html', {'news_list': news_list})


def news_detail_bootstrap(request):
    news = {}


def about(request):
    return render_to_response('news/about.html',{})