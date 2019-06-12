from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView, TemplateView
from graphene_django.views import GraphQLView
from meatriteApi.schema import schema
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('core/', include('mrCoreModels.urls')),
    path('stock/', include('mrStock.urls')),
    path('office/', include('mrAdminOffice.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
