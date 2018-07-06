from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductListDetailsView, ProcessedStockTimeView, InputStockView

urlpatterns = {
    path('', ProductListDetailsView.as_view(), name="details"),
    path('<stock>', ProcessedStockTimeView.as_view()),
    path('input', InputStockView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)