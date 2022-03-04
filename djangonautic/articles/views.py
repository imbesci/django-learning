from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    articlelist = Article.objects.all().order_by('date')
    contextdict = {
        'articlelist':articlelist
    }
    return render(request, "./articles/article_list.html", context=contextdict)

def article_detail(request, slug):
    article = Article.objects.get(slug= slug)
    return render(request, 'articles/article_detail.html', context={'article': article})

@login_required(redirect_field_name='auth_failed', login_url='accounts:login')
def article_create(request):
    if request.method == "POST":
        newpost = forms.CreateArticle(request.POST, request.FILES)
        if newpost.is_valid():
            instance = newpost.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        entryform = forms.CreateArticle()
    return render(request, 'articles/article_create.html', context = {'entryform' : entryform} )