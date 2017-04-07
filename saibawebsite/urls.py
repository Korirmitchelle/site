"""saibawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^merchant/register/', views.register_merchant, name='home'),
    url(r'^wallet/', views.wallet, name='home'),
    url(r'^overview/', views.overview, name='home'),
    url(r'^documentation/', views.documentation, name='home'),
    url(r'^about/', views.about, name='home'),
    url(r'^team/', views.team, name='home'),
    url(r'^contact/', views.contact, name='home'),
    url(r'^legal/', views.legal, name='home'),
    url(r'^blog/', views.blog, name='home'),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^blog/(?P<slug>[\w\-]+)/$', views.blog_category, name="category_detail"),



]
