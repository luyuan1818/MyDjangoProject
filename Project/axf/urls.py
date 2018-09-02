from django.conf.urls import url

from axf import views

app_name = 'axf'

urlpatterns = [

    url(r'^home/$', views.home, name="home"),
    url(r'^market/$', views.market, name="market"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^main/$', views.mine, name="main"),
    # url(r'^h/$', views.h, name="home"),
    # url(r'^ho/$', views.ho, name="home"),
]
