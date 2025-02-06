from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path("about-us/", views.about, name="about_us"),
    path('menu/', views.menu, name='menu'),
    path('aloqa/', views.contacts_view, name='biz_bn_aloqa'),
]
