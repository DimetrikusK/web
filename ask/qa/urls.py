from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.test),
    url(r'^$', views.main_page, name='main_page'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/', views.test),
    url(r'^popular/.*$', views.popular, name='popular'),
    url(r'^new/', views.test),
    url(r'^signup/', views.test)
]

