from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/archive', views.archived_post_list, name='archived_list'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('post/new/', views.post_new, name='new'),
    path('post/<int:pk>/edit', views.post_edit, name='edit'),
    path('post/<int:pk>/archive', views.archive_post, name='archive'),
]
