# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
from comments.models import Comments
from comments.forms import CommentForm


def index(request):
    # return HttpResponse('欢迎访问我的博客网站')
    post_list = Post.objects.all().order_by('-create_time')
    # return render(request, 'blog/index.html',
    #               context={'title': '我的博客', 'welcome': '欢迎来到我的博客网站'})

    # 查询对应的
    get_comments(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc', ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comments_list = post.comments_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    return render(request, 'blog/detail.html', context={'post': post, 'form': form, 'comments_list': comments_list})


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__month=month, create_time__year=year)
    get_comments(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    get_comments(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=t)
    get_comments(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 获取对应的 评论数
def get_comments(post_list):
    for item in post_list:
        item.countComments = len(item.comments_set.all())