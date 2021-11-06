# posts/admin.py
from django.contrib import admin
from django.conf import settings
from .models import Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    # Добавляем возможность менять группу прямо в списке
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
