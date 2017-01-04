from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.ClaimsView.as_view(), name='new-claim'),
]
