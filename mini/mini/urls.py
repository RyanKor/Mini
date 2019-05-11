"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from bbom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('edit/<int:post_pk>/', views.edit, name = 'edit'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
    path('detail/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^Food/(?P<menu_slug>[-\w]+)/$', views.menu_list, name='product_list_by_menu'),
    url(r'^Food/$', views.menu_list, name='menu_list'),
]
