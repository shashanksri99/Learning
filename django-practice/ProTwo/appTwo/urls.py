from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$',views.index, name='index_page'),
    url(r'^$',views.help, name='help_page'),
    #url(r'^$',views.index, name='index_page')
]
