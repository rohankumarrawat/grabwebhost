"""grabwebhost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from grabwebhost import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    re_path(r'^verify/$', views.verify, name='verify'),
    re_path(r'^forget/$', views.forget, name='forget'),
    re_path(r'^domainresult/$', views.domainresult, name='domainresult'),
    re_path(r'^domaincart/$', views.domaincart, name='domaincart'),
    re_path(r'^domainreview/$', views.domainreview, name='domainreview'),
    path('dashboard/',include('manager.urls')),
    path('features/',views.feature),
    path('services/',views.services),
    path('aboutus/',views.aboutus),
    path('prebuild/',views.prebuild),
    # path('domain/',views.domain),
    path('contact/',views.contact),
  
    path('tac/',views.tac),
    path('webdev/',views.webdev),
    path('webdevcustom/',views.webdevcustom),
    path('pap/',views.pap),
    path('refund/',views.refund),
    re_path(r'^paymentauth/$', views.paymentauth, name='paymentauth'),
    re_path(r'^paymentinformation/$', views.paymentinformation, name='paymentinformation'),
    re_path(r'^currentinvoice/$', views.currentinvoice, name='currentinvoice'),
    re_path(r'^paymentprocessing/$', views.paymentprocessing, name='paymentprocessing'),
    re_path(r'^paymentprocessingdomain/$', views.paymentprocessingdomain, name='paymentprocessingdomain'),
    path('faq/',views.faq),
    path('sharedhosting/',views.sharedhosting),
    path('reseller/',views.resellerhosting),
    re_path(r'^shared/$', views.shared, name='shared'),
    re_path(r'^predevelopedcheckout/$', views.predevelopedcheckout, name='predevelopedcheckout'),
  
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
