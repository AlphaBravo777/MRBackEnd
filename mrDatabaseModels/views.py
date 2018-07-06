from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductListSerializer, ProcessedStockSerializer, TestSerializer
from .models import Productlist, ProcessedStockAmounts, StockTakingTimes
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListDetailsView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Productlist.objects.all()
    serializer_class = ProductListSerializer 

class InputStockView(APIView):

    def post(self, request, format='json'):
        for key in request.data:
            value = request.data[key]
            obj = {'name': key, 'amount': value, 'time': '06:00'}
            # return Response(obj)
        serializer = TestSerializer(data = obj)
        if serializer.is_valid():
            # serializer.save()
            p = ProcessedStockAmounts(amount='33', prodName = Productlist.objects.get(productid = 'SV1'), time = StockTakingTimes.objects.get(times='06:00'))
            p.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        # return Response(resp)

class ProcessedStockTimeView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = ProcessedStockSerializer 

    def get_queryset(self):
        time = self.kwargs['stock']
        value = ProcessedStockAmounts.objects.filter(time__times__icontains=time)
        return value

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