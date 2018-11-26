from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TimeStampID

urlpatterns = [
    path('getTimeStampID/', TimeStampID.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)