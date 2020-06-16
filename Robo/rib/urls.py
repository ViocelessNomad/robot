# rib/urls.py

from django.urls import path
from .views import BlogListVievs, LearListView, ShopPageVievs, BlogDetailVievs, BlCreateView, BlUpdateView, BlDeleteView

urlpatterns = [
    path('shop/', ShopPageVievs.as_view(), name='shop'),
    path('learn/', LearListView.as_view(), name='learn'),
    path('post/<int:pk>/delete/', BlDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailVievs.as_view(), name='post_detail'),
    path('', BlogListVievs.as_view(), name='home'),

]
