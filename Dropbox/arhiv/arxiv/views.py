# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Article

def index(request):
	context = {Article.objects.all()}
	return render(request, 'arxiv/index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'arxiv/detail.html', {'articles': article})

def main(request):
    articles = Article.objects.all()
    return render(request, 'arxiv/main.html', {'articles': articles})



