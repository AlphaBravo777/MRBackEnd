"""meatriteApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    # url(r'^$', serve,kwargs={'path': 'index.html'}),
    # url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',RedirectView.as_view(url='/static/frontend/%(path)s', permanent=False)),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # re_path('.*', TemplateView.as_view(template_name='index.html')),
    # url(r'^', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),  This will add all kinds of site auth urls -
    # see https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication under "Project URLs"
]
