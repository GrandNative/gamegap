# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name='panel'),
    path('login', views.login_page, name='login'),
    path('khosh-galdin', views.last_page, name='end')
]
