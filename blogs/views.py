from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blogs.models import Blog, Post


class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    queryset = Blog.objects.all()
    paginate_by = 20


class BlogView(DetailView):
    template_name = "blogs/blog.html"
    queryset = Blog.objects.all()


class PostList(ListView):
    template_name = "blogs/post_list.html"
    queryset = Post.objects.all()
    paginate_by = 20


class PostView(DetailView):
    template_name = "blogs/post.html"
    queryset = Post.objects.all()
