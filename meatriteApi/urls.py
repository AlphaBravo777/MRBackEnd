from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView, TemplateView
from graphene_django.views import GraphQLView
from meatriteApi.schema import schema

urlpatterns = [
    # url(r'^$', serve,kwargs={'path': 'index.html'}),
    # url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',RedirectView.as_view(url='/static/frontend/%(path)s', permanent=False)),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # re_path('.*', TemplateView.as_view(template_name='index.html')),
    # url(r'^', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),  This will add all kinds of site auth urls -
    # see https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication under "Project URLs"
]
