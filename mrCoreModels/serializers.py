from rest_framework import serializers
from mrDatabaseModels.models import StockTakingTimes, TimeStamp, ProcessedStockAmounts

class TimeStampIDSerializer(serializers.ModelSerializer):

    # productid = serializers.StringRelatedField()
    # container = serializers.StringRelatedField(source='containernameid')

    class Meta:
        model = TimeStamp
        fields = '__all__'

class ProcessedStockAmountsSerializer(serializers.ModelSerializer):

    # productid = serializers.StringRelatedField()
    # container = serializers.StringRelatedField(source='containernameid')

    class Meta:
        model = ProcessedStockAmounts
        fields = '__all__'