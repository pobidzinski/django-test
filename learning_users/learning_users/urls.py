"""
Definition of urls for learning_users.
"""

from django.conf.urls import include, url
from basic_app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basic_app/', include('basic_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name='logout'),
]
