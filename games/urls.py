from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^snake', 'snake.views.snake', name='snake'),
    url(r'^register/$', 'snake.views.register', name='register'),
    url(r'^$', 'snake.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^profile/$', 'snake.views.profile', name='profile'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^save_score', 'snake.views.save_score', name='save_score'),
    url(r'^get_score', 'snake.views.get_score', name='get_score'),
    url(r'^leaderboard', 'snake.views.leaderboard', name='leaderboard'),

    url(r'^memory', 'snake.views.memory', name='memory'),


)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)