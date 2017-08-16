from django.conf.urls import url
from . import views

urlpatterns = [
# url(r'^$', views.index),
url(r'^loginPage$', views.loginPage),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^show_users$', views.show_all),
url(r'^user/(?P<id>\d+)$', views.user),
url(r'^logout$', views.logout),
url(r'^submit_algo$', views.submit_algo),
url(r'^submit_answer/(?P<page>\d+)$', views.submit_answer_nologin),
url(r'^submit_answer/(?P<id>\d+)/(?P<page>\d+)$', views.submit_answer),
# url(r'^page_test$', views.test_page),

url(r'^$', views.algo_view),
url(r'^level_two$', views.level_two),

    ]     
