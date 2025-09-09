from django.urls import path
from blog.views import post_list, post_detail, post_share, post_comment, post_search
from blog.feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('tag/<slug:tag_slug>/<int:page_number>', post_list, name='post_list_by_tag'),
    path('<int:page_number>/', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', post_search, name='post_search')
]