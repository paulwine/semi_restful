from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^add_user$', views.add_user),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^edit_user$', views.edit_user),
    url(r'^delete/(?P<user_id>\d+)$', views.delete)

]