from django.conf.urls import url

from views import home_page, post_detail

urlpatterns = [
    url(r'^', home_page, name = 'home'),
    url(r'^(?P<id>\d+)/$', post_detail, name = 'post_read')
]
