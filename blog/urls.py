"""misperris URL Configuration

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
from django.conf.urls import include, url
from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     
  url('perris', views.post_list , name= 'post_list'),  
  url('usuarios', views.post_list_user , name= 'post_list_user'), 
  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
  url(r'^post/new/$', views.post_new, name='post_new'),
  url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
  url(r'^$', views.inicio,name ='inicio'),
  #url(r'^post/agregar/$', views.post_addperro, name='post_addperro'),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  url('registro', views.registro , name= 'registro'),
  path('eliminar/<int:pk>', views.post_delete, name='post_delete'),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


