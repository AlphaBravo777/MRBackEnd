from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductListSerializer, ProcessedStockSerializer
from .models import Productlist, ProcessedStockAmounts

class ProductListDetailsView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Productlist.objects.all()
    serializer_class = ProductListSerializer 

class ProcessedStockTimeView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = ProcessedStockSerializer 

    def get_queryset(self):
        time = self.kwargs['stock']
        # return ProcessedStockAmounts.objects.filter(time=time)
        return ProcessedStockAmounts.objects.filter(time__times__icontains=time)

    # This changes the way the data is given through
    # def list(self, request, *args, **kwargs):
    #     response = super(ProcessedStockTimeView, self).list(request, *args, **kwargs) # call the original 'list'
    #     response.data = {"site": response.data} # customize the response data
    #     return response # return response with this custom representation

# >>> from mrDatabaseModels.models import ProcessedStockAmounts
# >>> ProcessedStockAmounts.objects.all()
# <QuerySet [<ProcessedStockAmounts: SV1>, <ProcessedStockAmounts: RV1>]>
# >>> ProcessedStockAmounts.objects.filter(time__times='06:00:00')
# <QuerySet [<ProcessedStockAmounts: SV1>, <ProcessedStockAmounts: RV1>]>
# >>> ProcessedStockAmounts.objects.filter(time__times='12:00:00')
# <QuerySet []>
# >>> ProcessedStockAmounts.objects.filter(time__times__contains='12')
# >>>