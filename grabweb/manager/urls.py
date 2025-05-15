"""grabwebhost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,re_path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index),
    re_path(r'^payinvoice/$', views.payinvoice, name='payinvoice'),
    path('login/', views.login_view),
    path('register/', views.register,name='register'),
    path('secondway/', views.secondway),
    path('forgot/', views.forgot),
    path('profile/', views.profile),
    path('privacy_profile/', views.profile2),
    path('openticket/', views.openticket),
    path('ticket/', views.ticket),
    path('blog/', views.blog),
    path('news/', views.news),
    path('changepassword/', views.changepassword),
    path('logout/', views.logout1),
    path('securitypin/', views.securitypin),
    path('invoice/', views.invoice),
  path('myservice/', views.myservice),
  path('mydomain/', views.mydomain),
 


   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
