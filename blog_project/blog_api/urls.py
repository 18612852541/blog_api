from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('api/', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]