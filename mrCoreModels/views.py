from django.shortcuts import render
from rest_framework import generics
from .serializers import TimeStampIDSerializer, ProcessedStockAmountsSerializer
from mrDatabaseModels.models import TimeStamp, StockTakingTimes, ProcessedStockAmounts, Productcontainers, Productlist, Productcontainernames
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

class TimeStampID(generics.ListCreateAPIView):

    serializer_class = TimeStampIDSerializer

    def get_queryset(self, format='json'):

        def createTimeStamp(obj):
            serializer = TimeStampIDSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
                return

        def createContianerIDs():
            group = ProcessedStockAmounts.objects.all()
            for stockItem in group:
                prodName = str(stockItem.prodName)
                container = str(stockItem.container)
                stockItemID = int(stockItem.id)
                prodNameID = Productlist.objects.get(productid=prodName)
                containerID = Productcontainernames.objects.get(containername=container)
                containerField = Productcontainers.objects.get(Q(productid=prodNameID.id) & Q(containernameid=containerID.id))
                obje = ProcessedStockAmounts.objects.get(id=stockItemID)
                print('here is the obj = ', obje)
                obje.prodContainer = containerField
                obje.save()
 
        # createContianerIDs()
        year = self.request.query_params.get('year')
        week = self.request.query_params.get('week')
        weekDay = self.request.query_params.get('weekDay')
        month = self.request.query_params.get('month')
        monthDay = self.request.query_params.get('monthDay')
        stringDay = self.request.query_params.get('stringDay')
        shift = self.request.query_params.get('shift')
        timeString = '06:00 (Paper)' # self.request.query_params.get('time')
        time = StockTakingTimes.objects.get(times=timeString)
        shortDate = self.request.query_params.get('shortDate')
        longDate = self.request.query_params.get('longDate')
        print(year, week, weekDay)
        instance = TimeStamp.objects.filter(Q(year=year) & Q(week=week) & Q(weekDay=weekDay))
        if not instance:
            obj = {'year': year, 'week': week, 'weekDay': weekDay, 'month': month, 'monthDay': monthDay, 'stringDay': stringDay, 'shift': shift, 'time': time.id, 'shortDate': shortDate, 'longDate': longDate,}
            createTimeStamp(obj)
            instance = TimeStamp.objects.filter(Q(year=year) & Q(week=week) & Q(weekDay=weekDay))
            return instance
        else:
            print('The id is ', instance)
            return instance


        # def post(self, request, format='json'):

        # def updateHighRiskPackingList(obj):
        #     record = HighRiskPackingList.objects.get(productCode=obj['prodName'])
        #     record.currentStock = record.currentStock + obj['amount']
        #     record.save()
        #     print('currentStock = ', record.currentStock, obj['amount'])
        #     pass

        # prodName = request.data.get('prodName')
        # time = request.data.get('time')
        # amount = request.data.get('amount')
        # container = request.data.get('container')
        # prodField = Productlist.objects.get(productid=prodName)
        # timeField = StockTakingTimes.objects.get(times=time)
        # containerField = Productcontainernames.objects.get(containername=container)
        # instance = ProcessedStockAmounts.objects.filter(Q(time=timeField.id) & Q(prodName=prodField.id) & Q(container=containerField.id))
        # obj = {'amount': amount, 'prodName': prodField.id, 'time': timeField.id, 'container': containerField.id}
        # updateHighRiskPackingList(obj)
        # print(timeField.id, prodField.id, containerField.id)
        # print(obj)
        # instance.delete()
        # serializer = ProcessedStockAmountsSerializer(data = obj)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)