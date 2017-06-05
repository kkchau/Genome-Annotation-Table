"""cse182 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import anno_table.views

urlpatterns = [
    url(r'^$', anno_table.views.base, name='base_view'),
    url(r'^raw/([0-9a-zA-Z]+)/$', anno_table.views.raw_disp, name='raw_display'),
    url(r'^download/$', anno_table.views.download, name='download_display'),
    url(r'^admin/', admin.site.urls),
]
