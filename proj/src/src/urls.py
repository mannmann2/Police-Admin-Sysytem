"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static  import static
from django.contrib import admin 
import app1.views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

	url(r'^$', app1.views.home, name='home'),
    
    url(r'^trafficreg/$', app1.views.traffic, name='traffic'),
    url(r'^trafficpay/$', app1.views.traffic2, name='traffic2'),
    url(r'^FIR/$', app1.views.FIR, name='FIR'),
    url(r'^wanted/$', app1.views.wanted, name='wanted'),
    url(r'^pass/$', app1.views.passp, name='passp'),

    url(r'^profile/$', app1.views.profile, name='profile'),
    
    url(r'^contact/$', app1.views.contact, name='contact'),
    url(r'^about/$', app1.views.about, name='about'),
    
    url(r'^messages/$', app1.views.messages, name='mess'),
    
    url(r'^accounts/', include('registration.backends.default.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)







