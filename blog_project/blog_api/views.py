from rest_framework import generics
from . import models
from . import serializers
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


def post_list(request):
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




# class TryList(generics.ListAPIView):
#    queryset = models.Try.objects.all()
#    serializer_class = serializers.TrySerializer
#
# class TryDetail(generics.RetrieveAPIView):
#    queryset = models.Try.objects.all()
#    serializer_class = serializers.TrySerializer
#
#
# class TryDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = models.Try.objects.all()
#    serializer_class = serializers.TrySerializer
