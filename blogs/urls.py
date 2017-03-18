from django.conf.urls import url
from.views import BlogList, BlogView, PostList, PostView

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="allblogs"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^(?P<pk>\d+)/posts/$', PostList.as_view(), name="posts"),
    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="onepost")
]