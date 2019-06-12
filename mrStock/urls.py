from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  CreateOrUpdateProcStock, ChangeContainerRankings, GetSelectiveDeleteData, UpdateHppMeatriteStock, DeleteHppMeatriteStock

urlpatterns = [
    path('procStock/update/', CreateOrUpdateProcStock.as_view()),
    path('containerRankings/update/', ChangeContainerRankings.as_view()),
    path('getSelectiveDeleteData', GetSelectiveDeleteData.as_view()),
    path('hppStock/update/', UpdateHppMeatriteStock.as_view()),
    path('hppStock/deleteGroup/<productStatusid>', DeleteHppMeatriteStock.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)