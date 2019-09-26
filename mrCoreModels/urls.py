from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateTimeStampID, GetTimeStampDetails, GetAllTimeStampsForWeekNo

# 192.168.2.25:8080/core/
urlpatterns = [
    path('createTimeStampID/', CreateTimeStampID.as_view()),
    path('getTimeStampDetails/<pk>', GetTimeStampDetails.as_view()),
    path('getAllTimeStampidsForWeekNo/<pk>', GetAllTimeStampsForWeekNo.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)