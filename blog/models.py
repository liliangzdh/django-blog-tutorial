
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章内容
    body = models.TextField()
    # 文章创建时间
    create_time = models.DateTimeField()
    # 文章修改时间
    modified_time = models.DateTimeField()
    # 文章摘要  blank=True 参数值后就可以允许空值了
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类 （文章只有一个分类）
    category = models.ForeignKey(Category)

    # 标签 文章可以有 多个标签，标签可以有多个文章
    tag = models.ManyToManyField(Tag, blank=True)

    # 作者  文章作者，这里 User 是从 django.contrib.auth.models 导入的
    # django.contrib.auth 是 Django 内置的应用，
    # 专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # pk 代表 primekey
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

