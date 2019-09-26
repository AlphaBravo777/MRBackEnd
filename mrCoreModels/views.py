from django.shortcuts import render
from rest_framework import generics
from .serializers import NewTimeStampIDSerializer
from mrDatabaseModels.models import TimeStamp, StockTakingTimes, ProcessedStockAmounts, Productcontainers, Productlist, Productcontainernames, Shifts

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

class CreateTimeStampID(generics.ListCreateAPIView):   

    def post(self, request, format='json'):

        def createTimeStamp(obj):
            serializer = NewTimeStampIDSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        year = self.request.data.get('year')
        week = self.request.data.get('week')
        weekDay = self.request.data.get('weekDay')
        shiftString = self.request.data.get('shift')
        shortDate = self.request.data.get('shortDate')
        shift = Shifts.objects.get(shiftName=shiftString)
        timeString = self.request.data.get('time')
        time = StockTakingTimes.objects.get(times=timeString)
        obj = {'year': year, 'week': week, 'weekDay': weekDay, 'shift': shift.id, 'time': time.id, 'shortDate': shortDate}
        success = createTimeStamp(obj)
        return success

class GetTimeStampDetails(generics.ListCreateAPIView):

    serializer_class = NewTimeStampIDSerializer
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['pk']
        returnValue = TimeStamp.objects.filter(id=id)
        return returnValue

class GetAllTimeStampsForWeekNo(generics.ListCreateAPIView):

    serializer_class = NewTimeStampIDSerializer
    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['pk']
        returnValue = TimeStamp.objects.get(id=id)
        weekNo = returnValue.week
        # weekNo = 38
        shift = returnValue.shift
        time = returnValue.time
        weekValues = TimeStamp.objects.filter(Q(week=weekNo, shift=shift.id, time=time.id) | \
        Q(week=weekNo+1, shift=shift.id, time=time.id, weekDay=1)).exclude(week=weekNo, weekDay=1)
        print(' - - - ', weekValues)
        return weekValues