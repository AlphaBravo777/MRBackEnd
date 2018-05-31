from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api import views
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/users/register', views.UserCreate.as_view(), name='account-create'),
    path('api/users/login', views.UserLogin.as_view(), name='account-login'),
    url(r'^', include(router.urls)),
    #url(r'users^$', views.UserCreate.as_view(), name='account-create'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
