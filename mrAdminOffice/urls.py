from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InsertNewReport, WholeDayTimeStamp, DeleteReportEntry, InsertNewChecklist, InsertNewClientAccount

urlpatterns = [  # meatrite.com/office/
    path('report/enterNew/', InsertNewReport.as_view()),
    path('timeStamp/wholeDay/', WholeDayTimeStamp.as_view()),
    path('report/deleteReport/<id>', DeleteReportEntry.as_view()),
    path('checklists/enterNew/', InsertNewChecklist.as_view()),
    path('accounts/enterNew/',  InsertNewClientAccount.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)