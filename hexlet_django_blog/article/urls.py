from django.urls import path
from.views import index

urlpatterns = [
    path('', index, name='index'),
    path('<str:tags>/<int:article_id>', index, name='article'),
]

"""
# project.users.urls
from django.urls import path

from project.users import views

urlpatterns = [
    path('', views.users_view),
    path('<int:user_id>/pets/<int:pet_id>/med_info/', views.pet_med_info_view),
    …
]
Сделайте так, чтобы hexlet_django_blog.article.views.index 
принимала строковый параметр "tags" и целочисленный параметр 
"article_id" из пути /articles/tags/article_id и выводила текст 
в виде Статья номер 42. Тег python
"""