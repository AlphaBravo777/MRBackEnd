from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  ProductListDetailsView, \
                    ProcessedStockTimeView, \
                    InsertMultiProcessedStock, \
                    DeleteProcessedStockTime, \
                    GetProductContainers, \
                    TestDelete, \
                    DeleteSpecifiedContainers, \
                    UpdateContainerDelete, \
                    GetStockTimes, \
                    ProductUpdateAmount

urlpatterns = [
    path('delete/containers/<containers>', DeleteSpecifiedContainers.as_view()),
    path('delete/containerUpdate/<pk>', UpdateContainerDelete.as_view()),
    path('delete/<deleteTime>', DeleteProcessedStockTime.as_view()),
    path('product/updateSingleAmount/', ProductUpdateAmount.as_view()),
    path('testDelete/', TestDelete.as_view()),
    path('containers/', GetProductContainers.as_view()),
    path('input/', InsertMultiProcessedStock.as_view()),
    path('getStockTimes/', GetStockTimes.as_view(), name="getStockTimes"),
    path('<str:stockT>/', ProcessedStockTimeView.as_view(), name="stockstime"),
    path('', ProductListDetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
