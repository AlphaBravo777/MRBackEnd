from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductListDetailsView, ProcessedStockTimeView, InsertMultiProcessedStock, DeleteProcessedStockTime

urlpatterns = {
    path('', ProductListDetailsView.as_view(), name="details"),
    path('<stock>', ProcessedStockTimeView.as_view()),
    path('input/', InsertMultiProcessedStock.as_view()),
    path('delete/<deleteTime>', DeleteProcessedStockTime.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)