from django.urls import path
from .views import post_detail,post_list,post_share, post_search
from .feeds import LatestPostFeed

app_name='blog'
urlpatterns=[
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name="postdetail"),
	path('<int:post_id>/share/', post_share, name='postshare'),
	path('', post_list, name='postlist'),
	path("tag/<slug:tag_slug>/", post_list, name='postlist_by_tag'),
	path('feed/', LatestPostFeed(), name='post_feed'),
	path('blog/post/search', post_search, name="post_search")

	#path('', PostListView.as_view(), name='postlist'),
]