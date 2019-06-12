from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InsertNewReport, \
        WholeDayTimeStamp, \
        DeleteReportEntry, \
        InsertNewChecklist, \
        InsertNewClientAccount, \
        UpdateReport, \
        DailyReportImages, \
        InsertNewOrderDetails, \
        InsertOrderProductAmounts

urlpatterns = [  # meatrite.com/office/
    path('report/enterNew/', InsertNewReport.as_view()),
    path('report/update/<pk>', UpdateReport.as_view()),
    path('report/deleteReport/<id>', DeleteReportEntry.as_view()),
    path('report/insertImage/', DailyReportImages.as_view()),
    path('report/downloadImage/', DailyReportImages.as_view()),
    path('timeStamp/wholeDay/', WholeDayTimeStamp.as_view()),
    path('checklists/enterNew/', InsertNewChecklist.as_view()),
    path('accounts/enterNew/',  InsertNewClientAccount.as_view()),
    path('orders/enterDetails/',  InsertNewOrderDetails.as_view()),
    path('orders/enterProductAmounts/',  InsertOrderProductAmounts.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)