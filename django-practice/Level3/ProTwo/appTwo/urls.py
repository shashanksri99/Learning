from django.conf.urls import url
from appTwo import views


urlpatterns = [
    url(r'^$',views.users, name ='users'),
    url(r'^$',views.form_page, name ='form'),
    url(r'^$',views.index, name ='index'),
]
