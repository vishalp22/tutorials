"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
import myproject.urls
import myproject.urls_categories
from webproject import settings
from sharpurskill.views import single_product, category_grid, authentication, Contact_Us
from myproject.views import course_model_form
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^single-product/$', single_product, name='single-product'),
    url(r'^category-grid/$', category_grid, name='category-grid'),
    url(r'^authentication/$', authentication, name='authentication'),
    # url(r'^sample/$', 'sharpurskill.views.sample', name='sample'),
    url(r'^contact/$', Contact_Us, name='contact'),
    url(r'^submit/$', course_model_form, name='submit'),
    # url(r'^submit_img/$', image_model_form, name='submit_img'),

    url(r'^search/', include('haystack.urls'), name='search'),
    url(r'', include(myproject.urls)),
    url(r'', include(myproject.urls_categories)),

    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
