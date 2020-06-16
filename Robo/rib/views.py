from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class BlogListVievs(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailVievs(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class LearListView (TemplateView):
    template_name = 'lear.html'


class ShopPageVievs(TemplateView):
    template_name = 'shop.html'
# Create your views here.
