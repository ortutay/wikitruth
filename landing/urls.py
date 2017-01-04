from django.conf.urls import url

from landing import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^signin$', views.SigninView.as_view(), name='signin'),
    url(r'^signup$', views.SignupView.as_view(), name='signup'),
]
