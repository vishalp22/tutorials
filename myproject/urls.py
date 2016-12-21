from django.conf.urls import url
from .views import WebDevelopmentDetailView

urlpatterns = [
    # url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/$', WebDevelopmentDetailView.as_view(), name='single-product'),
    # url(r'^web_development/$', 'technology.views.web_development', name='web_development'),
    # url(r'^sample/$', WebDevelopmentListView.as_view(), name='sample'),
    # url(r'^web_development/$', WebDevelopmentListView.as_view(), name='category_detail'),

    # url(r'^$', WebDevelopmentListView.as_view(), name='category_detail'),
    #    url(r'^mobile_apps/$', MobileAppsListView.as_view(), name='mobile_app'),
    #    url(r'^mobile_apps/(?P<pk>\d+)/$', MobileAppsDetailView.as_view(), name='single-product'),

    #    url(r'^programming_language/$', ProgramingLanguageListView.as_view(), name='programming_language'),
    #    url(r'^programming_language/(?P<pk>\d+)/$', ProgrammingLanguageDetailView.as_view(), name='single-product'),

]
