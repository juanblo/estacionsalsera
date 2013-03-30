#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# Static content for development
urlpatterns = staticfiles_urlpatterns()

# Serve media for development
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += patterns(
    '',

    # Home
    url(
        r'^$',
        'app.views.home',
        name='home',
    ),
)
