from django.shortcuts import get_object_or_404, render

from .models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context)


# Cтраницы, на которых будут посты, отфильтрованные по группам
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.group.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
