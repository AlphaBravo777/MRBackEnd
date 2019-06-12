from django.shortcuts import render
from rest_framework import generics
from .serializers import CreateOrUpdateProcStockSerializer, HPPMeatriteStockSerializer
from mrDatabaseModels.serializers import ProcessedStockAmountsSerializer
from .models import HPPProductStatus, HPPMeatriteStock

from mrDatabaseModels.models import ProcessedStockAmounts, TimeStamp, Productcontainers, Productlist, Productcontainernames, Factoryarea
from mrCoreModels.models import SettingsDB
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class CreateOrUpdateProcStock(generics.UpdateAPIView):

    def post(self, request, format='json'):

        def updateProductAmount(): # This is an existing instance (already serialized) that we are changing, so we can not use a serializer

            instance = ProcessedStockAmounts.objects.get(Q(timeStampID=timeInstance) & Q(prodContainer=prodContainerID))
            if item['amount'] == '' or item['amount'] == '0':
                instance.delete()
            else:    
                instance.amount = item['amount']
                instance.save()

        def createProductAmount():# This is a new object that we are creating, so we must serialize it first
            serializer = CreateOrUpdateProcStockSerializer(data = obj)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def setLastTimeStampUsed():
            timeRecord = SettingsDB.objects.get(id=1)
            timeRecord.value1 = timeInstance.id
            timeRecord.value2 = dbTimeID
            timeRecord.save()

        dbTimeid = request.data.get('timeid')
        dbTimeID = request.data.get('timeID')
        data = request.data.get('data')
        timeInstance = TimeStamp.objects.get(id=dbTimeid)
        setLastTimeStampUsed()
        for item in data:
            prodContainerID = Productcontainers.objects.get(id=item['databaseID'])
            productid = Productlist.objects.get(productid=prodContainerID.productid)
            productContianerNameID = Productcontainernames.objects.get(containername=prodContainerID.containernameid)
            instance = ProcessedStockAmounts.objects.filter(Q(timeStampID=timeInstance) & Q(prodContainer=prodContainerID))[:1]
            obj = {'amount': item['amount'], 'prodName': productid.id, 'container': productContianerNameID.id, 'user': request.user.id, 'timeStampID': timeInstance.id , 'prodContainer': prodContainerID.id}
            if instance:
                updateProductAmount()
            else:
                createProductAmount()
        return Response(True, status=status.HTTP_201_CREATED)

class ChangeContainerRankings(generics.UpdateAPIView):

    def post(self, request, format='json'):

        factoryCatagoryName = request.data['factoryCatagory']
        factoryCatagory = Factoryarea.objects.get(area=factoryCatagoryName)
        data = request.data['newList']
        x = 1
        for item in data:
            instance = Productcontainers.objects.get(id=item['databaseID'])
            instance.factoryRanking = x
            instance.factoryCatagory = factoryCatagory
            # print('--------------- ', instance.factoryRanking, instance.factoryCatagory.area)
            instance.save()
            x = x + 1
        return Response('success', status=status.HTTP_201_CREATED)

class GetSelectiveDeleteData(generics.ListAPIView):
    #probably not going to use this view
    serializer_class = ProcessedStockAmountsSerializer

    def get_queryset(self, format='json'):
        timeRecord = SettingsDB.objects.get(id=1)
        fetchPreviousData = ProcessedStockAmounts.objects.filter(Q(timeStampID=timeRecord.id) & Q(prodContainer__deleteContainerAmount=False))
        return fetchPreviousData
        
class UpdateHppMeatriteStock(generics.ListCreateAPIView):

    def post(self, request, format='json'):

        productStatusid = request.data[0]['productStatusid']
        # print("Here is the update MeatriteHppStock: ", request.data[0]['productStatusid'])
        HPPMeatriteStock.objects.filter(productStatusid=productStatusid).delete()

        serializer = HPPMeatriteStockSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteHppMeatriteStock(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        productStatusid = self.kwargs['productStatusid']
        # print("Here is the delete data ", productStatusid)
        HPPMeatriteStock.objects.filter(productStatusid=productStatusid).delete()
        return Response(True, status=status.HTTP_201_CREATED)

