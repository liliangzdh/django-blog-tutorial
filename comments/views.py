from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comments
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # request.POST :这个表示 提交的内容
        form = CommentForm(request.POST)
        # is_valid 这个会自己效验
        if form.is_valid():
            # 效验成功
            # commit=False 的作用是仅仅利用表单的数据生成 Comments 模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)
            #
            comment.post = post
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            #数据不合法
            #因为  Post 和Comments 是 ForeignKey关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            comment_list = post.comments_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)

    # redirect 重定向
    return redirect(post)
