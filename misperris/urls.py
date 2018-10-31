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
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    path('usuario/', include('usuario.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
    path('pass-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/pass_reset.html'
         ),
         name='pass_reset'), 
    path('pass-reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='pass_reset_done'),
    path('pass-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/pass_reset_confirm.html'
         ),
         name='pass_reset_confirm'),
    path('pass-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/pass_reset_complete.html'
         ),
         name='pass_reset_complete'),
]
