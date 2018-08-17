from django.shortcuts import render
from rest_framework import generics
from .serializers import    ProductListSerializer,\
                            ProcessedStockSerializer,\
                            TestSerializer,\
                            ProcessedStockSerializer2,\
                            Productcontainers,\
                            ProductContainersSerializer
from .models import Productlist, ProcessedStockAmounts, StockTakingTimes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductListDetailsView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Productlist.objects.filter(productonhold=False).order_by("brand", "unitweight")
    serializer_class = ProductListSerializer 

class GetProductContainers(generics.ListCreateAPIView):

    queryset = Productcontainers.objects.order_by("productid", "containernameid")
    serializer_class = ProductContainersSerializer 

class ProcessedStockTimeView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = ProcessedStockSerializer

    def get_queryset(self, format='json'):
        time = self.kwargs['stockT']
        value = ProcessedStockAmounts.objects.filter(time__times__icontains=time)
        return value


class InsertMultiProcessedStock(APIView):

    def post(self, request, format='json'):

        serializer = TestSerializer(data = request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProcessedStockTime(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        time = self.kwargs['deleteTime']
        values = ProcessedStockAmounts.objects.filter(time__times__icontains=time)
        values.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class TestDelete(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        values = ProcessedStockAmounts.objects.filter(time__times__icontains='00:11')
        values.delete()
        return Response('true', status=status.HTTP_204_NO_CONTENT) 

    # class InputStockView(APIView):

#     def post(self, request, format='json'):
#         for key in request.data:
#             value = request.data[key]
#             obj = {'name': key, 'amount': value, 'time': '06:00'}
#             # return Response(obj)
#         serializer = TestSerializer(data = obj)
#         if serializer.is_valid():
#             # serializer.save()
#             p = ProcessedStockAmounts(amount='33', prodName = Productlist.objects.get(productid = 'SV1'), time = StockTakingTimes.objects.get(times='06:00'))
#             p.save()
#             return Response(serializer.data)
#         else: 
#             return Response(serializer.errors)
#         # return Response(resp)