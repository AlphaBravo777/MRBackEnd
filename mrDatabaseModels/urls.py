from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductListDetailsView 

urlpatterns = {
    path('', ProductListDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)