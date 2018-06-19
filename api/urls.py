from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api import views
from . import views
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/users/register', views.UserCreate.as_view(), name='account-create'),
    path('api/users/login', views.UserLogin.as_view(), name='account-login'),
    path('products/', include('mrDatabaseModels.urls')),
    path('test/', views.GetGroups.as_view(), name='getGroupNames'),
    #url(r'^', include('api.urls')) # Add this line
    url(r'^', include(router.urls)),
    #url(r'users^$', views.UserCreate.as_view(), name='account-create'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
