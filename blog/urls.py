from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('post/<int:post_id>/<slug:slug>/', views.post_detail, name='post-detail'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<slug:slug>/', views.posts_by_tag, name='posts-by-tag'),
    path('course-reviews/', TemplateView.as_view(template_name='blog/course_reviews.html'), name='course-reviews'),
    path('revealjs/', TemplateView.as_view(template_name='blog/revealjs.html'), name='revealjs'),
    path('sql-intro/', TemplateView.as_view(template_name='blog/intro_to_sql.html'), name='sql-intro'),
]