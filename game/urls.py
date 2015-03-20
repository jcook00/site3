from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'game.views.home', name='home'),
    url(r'^home2/$', 'game.views.home2', name='home'),
    url(r'^home3/$', 'game.views.home2', name='home'),
    url(r'^home4/$', 'game.views.home2', name='home'),
    url(r'^home5/$', 'game.views.home2', name='home'),
    url(r'^home6/$', 'game.views.home2', name='home'),
    #url(r'^rpg/', include('rpg.urls', namespace="rpg")),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^rpg/', include('rpg.urls')),
    url(r'^admin/', include(admin.site.urls)),
)