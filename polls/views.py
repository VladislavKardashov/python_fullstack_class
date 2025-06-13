from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from polls.models import Post


# Create your views here.

class PostDetailView(DetailView):
    model = Post
    
    
    
class PostListView(ListView):
    model = Post
    