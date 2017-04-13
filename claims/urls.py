from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.NewClaimsView.as_view(), name='new-claim'),
    url(r'^$', views.claims, name='claims'),
    url(r'^(?P<id>[0-9]+)$', views.ClaimDetail.as_view(), name='claim-detail'),
    url(r'^responses/(?P<id>[0-9]+)$', views.ResponseDetail.as_view(), name='response-detail'),
    url(r'^search$', views.search, name='search'),
]
