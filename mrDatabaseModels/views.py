from django.shortcuts import render
from rest_framework import generics
from .serializers import    ProductListSerializer,\
                            ProcessedStockSerializer,\
                            TestSerializer,\
                            ProcessedStockSerializer2,\
                            Productcontainers,\
                            ProductContainersSerializer, \
                            GetStockTimesSerializer, \
                            ProcessedStockAmountsSerializer
from .models import Productlist, ProcessedStockAmounts, StockTakingTimes, Productcontainernames, HighRiskPackingList
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

import logging
logger = logging.getLogger(__name__)

def infoMessage(message):
    # This does not really work in cmd promt
	logger.info('* * * * * * * * * = ' + message)

def errorMessage(message):
    # This one does show up on cmd promt
	logger.error(message)

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

class DeleteSpecifiedContainers(generics.ListCreateAPIView):

    serializer_class = ProductContainersSerializer
    def get_queryset(self, format='json', *kwargs):
        value = self.kwargs['containers']
        if value == 'half':
            returnValue = Productcontainers.objects.filter(deleteContainerAmount = 0)
            print(returnValue)
            return returnValue

class UpdateContainerDelete(generics.UpdateAPIView):

    queryset = Productcontainers.objects.all()
    # lookup_field = 'pk'
    serializer_class = ProductContainersSerializer

    # def get_queryset(self):
    #     id = self.request.data.get("delete")
    #     return Productcontainers.objects.filter(id=id)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get("delete") == 'true':
            boolValue = True
        else:
            boolValue = False
        print(boolValue, instance.deleteContainerAmount)
        instance.deleteContainerAmount = boolValue
        instance.save()

        # serializer = ProductContainersSerializer(data = instance)
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)

        return Response(data=None)

class GetStockTimes(generics.ListCreateAPIView):
    # infoMessage('I am running')
    # errorMessage('---- I am running')
    queryset = StockTakingTimes.objects.all()
    serializer_class = GetStockTimesSerializer 

class ProductUpdateAmount(generics.UpdateAPIView):
    # queryset = ProcessedStockAmounts.objects.all()
    # serializer_class = ProcessedStockAmountsSerializer

    def post(self, request, format='json'):

        def updateHighRiskPackingList(obj):
            record = HighRiskPackingList.objects.get(productCode=obj['prodName'])
            record.currentStock = record.currentStock + obj['amount']
            record.save()
            print('currentStock = ', record.currentStock, obj['amount'])
            pass

        prodName = request.data.get('prodName')
        time = request.data.get('time')
        amount = request.data.get('amount')
        container = request.data.get('container')
        prodField = Productlist.objects.get(productid=prodName)
        timeField = StockTakingTimes.objects.get(times=time)
        containerField = Productcontainernames.objects.get(containername=container)
        instance = ProcessedStockAmounts.objects.filter(Q(time=timeField.id) & Q(prodName=prodField.id) & Q(container=containerField.id))
        obj = {'amount': amount, 'prodName': prodField.id, 'time': timeField.id, 'container': containerField.id}
        updateHighRiskPackingList(obj)
        print(timeField.id, prodField.id, containerField.id)
        print(obj)
        instance.delete()
        serializer = ProcessedStockAmountsSerializer(data = obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.name = request.data.get("name")
    #     instance.save()

    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     return Response(serializer.data)


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