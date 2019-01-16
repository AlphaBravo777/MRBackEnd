from django.shortcuts import render
from rest_framework import generics
from mrCoreModels.serializers import NewTimeStampIDSerializer
from mrDatabaseModels.models import TimeStamp, StockTakingTimes, ProcessedStockAmounts, Productcontainers, Productlist, Productcontainernames, DaysOfTheWeek, Shifts
from .models import MessageLevels, DailyReport, ChecklistAreas
from .serializers import DailyReportSerializer, ChecklistSerializer, NewClientAccountSerializer
from mrDatabaseModels.serializers import TimeStampSerializer
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



def getOrCreateWholeDayTimeStampID(currentTimeStampid):

    def createTimeStamp(obj):
        serializer = TimeStampIDSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return
        else:
            print('Serializer is not valid', serializer)

    
    if currentTimeStampid != None:
        timestampInstance = TimeStamp.objects.get(id=currentTimeStampid)
        # print('* * * * * * * this is before the error2', timestampInstance )
        weekdayInstance = DaysOfTheWeek.objects.get(weekDayNames=timestampInstance.weekDay)
        # print('* * * * * * * this is before the error3', weekdayInstance)
        instance = TimeStamp.objects.filter(Q(year=timestampInstance.year) & Q(week=timestampInstance.week) & Q(weekDay=weekdayInstance.id) & Q(time=10) & Q(shift=4))
        if not instance:
            shiftInstance = Shifts.objects.get(id=4)
            wholeDayTime = StockTakingTimes.objects.get(id=10)
            obj = {'year': timestampInstance.year, 'week': timestampInstance.week, 'weekDay': timestampInstance.weekDay.id, 'shift': shiftInstance.id, 'time': wholeDayTime.id }
            createTimeStamp(obj)
            instance = TimeStamp.objects.get(Q(year=timestampInstance.year) & Q(week=timestampInstance.week) & Q(weekDay=timestampInstance.weekDay) & Q(time=10) & Q(shift=4))
            return instance
        else:
            instance = TimeStamp.objects.get(Q(year=timestampInstance.year) & Q(week=timestampInstance.week) & Q(weekDay=timestampInstance.weekDay) & Q(time=10) & Q(shift=4))
            return instance
    return

class InsertNewReport(generics.ListCreateAPIView):

    def post(self, request, format='json'):

        userInstance = self.request.user
        timestampid = request.data.get('timestampID')
        wholeDayTimestampInstance = getOrCreateWholeDayTimeStampID(timestampid)
        print('*** ', wholeDayTimestampInstance)
        message = request.data.get('message')
        messageLevel = request.data.get('messageLevel')
        messageLevelInstance = MessageLevels.objects.get(levelName=messageLevel)
        replyid = request.data.get('reply')
        if replyid:
            replyInstance = DailyReport.objects.get(id=replyid)
            obj = {'message': message, 'messageLevel': messageLevelInstance.id, 'user': userInstance.id, 'timeStampID': wholeDayTimestampInstance.id, 'reply': replyInstance.id}
        else: 
            obj = {'message': message, 'messageLevel': messageLevelInstance.id, 'user': userInstance.id, 'timeStampID': wholeDayTimestampInstance.id}
        serializer = DailyReportSerializer(data=obj)
        if serializer.is_valid():
            print('* * * * * serializer is valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WholeDayTimeStamp(generics.ListCreateAPIView):

    def get(self, format='json'):  # use get for a single record, and get_queryset for multiple records
        year = self.request.query_params.get('year')
        if year == None:
            year = 2018
        week = self.request.query_params.get('week')
        if week == None:
            week = 50
        weekDay = self.request.query_params.get('weekDay')
        if weekDay == None:
            weekDay = 1
        currentTimeStampid = self.request.query_params.get('id')
        wholeDayTimestampInstance = getOrCreateWholeDayTimeStampID(currentTimeStampid)
        print('* * * * * * * We are making it up till here', wholeDayTimestampInstance)
        if wholeDayTimestampInstance != None:
            # wholeDayTimeInstance = StockTakingTimes.objects.get(id=10)
            # weekdayInstance = DaysOfTheWeek.objects.get(id=weekDay)
            print('* * * * * * *, Here is the timestamp data: ', year, week, weekDay)
            wholedayTimeStampInstance = TimeStamp.objects.get(Q(year=year) & Q(week=week) & Q(weekDay=weekDay) & Q(time=10)& Q(shift=4))
            serializer = TimeStampSerializer(wholedayTimeStampInstance)
            print('======', wholedayTimeStampInstance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None)

class DeleteReportEntry(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        reportid = self.kwargs['id']
        print('The id = ', reportid)
        value = DailyReport.objects.get(id=reportid)
        value.delete()
        return Response('true', status=status.HTTP_204_NO_CONTENT) 

class InsertNewChecklist(generics.ListCreateAPIView):

    def post(self, request, format='json'):

        userInstance = self.request.user
        timestampid = request.data.get('timestampID')
        wholeDayTimestampInstance = getOrCreateWholeDayTimeStampID(timestampid)
        print('*** ', request.data.get('areaid'))
        message = request.data.get('message')
        messageLevel = request.data.get('messageLevel')
        messageAreaid = request.data.get('areaid')
        messageLevelInstance = MessageLevels.objects.get(levelName=messageLevel)
        messageAreaInstance = ChecklistAreas.objects.get(id=messageAreaid)
        obj = {'message': message, 'importance': messageLevelInstance.id, 'area': messageAreaInstance.id, 'user': userInstance.id, 'timeStampID': wholeDayTimestampInstance.id}
        print('*** ', obj)
        serializer = ChecklistSerializer(data=obj)
        if serializer.is_valid():
            print('* * * * * serializer is valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InsertNewClientAccount(generics.ListCreateAPIView):  
    # This does all the same as the above code, if the object property names that comes in is the same as the db field names

    def post(self, request, format='json'):

        print("Here is the data: ", request.data)
        serializer = NewClientAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)