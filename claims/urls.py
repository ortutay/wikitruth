from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.NewClaimsView.as_view(), name='new-claim'),
    url(r'^$', views.claims, name='claims'),
    url(r'^(?P<id>[0-9]+)$', views.ClaimDetail.as_view(), name='claim-detail'),
]
