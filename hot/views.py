from django.shortcuts import render, get_object_or_404
from .models import ArticleBrief

# Create your views here.
def index(request):
    latest_article_list = ArticleBrief.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'hot/index.html', context)

def detail(request, article_id):
    articlebrief = get_object_or_404(ArticleBrief, pk=article_id)
    context = {'articlebrief': articlebrief}
    return render(request, 'hot/detail.html', context)
