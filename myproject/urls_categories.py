from django.conf.urls import url, include
from .views import CategoryListView, CategoryDetailView, WebDevelopmentDetailView, TopDiscountList, \
    RecentlyUpdatedList

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='index'),
    url(r'^recently-updated-list/$', RecentlyUpdatedList.as_view(), name='recently_added'),
    url(r'^top-discount-list/$', TopDiscountList.as_view(), name='top_discount'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/$', WebDevelopmentDetailView.as_view(), name='single-product'),




]
