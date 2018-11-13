from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  CreateOrUpdateProcStock, ChangeContainerRankings

urlpatterns = [
    path('procStock/update/', CreateOrUpdateProcStock.as_view()),
    path('containerRankings/update/', ChangeContainerRankings.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)