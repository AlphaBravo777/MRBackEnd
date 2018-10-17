from rest_framework import serializers
from mrDatabaseModels.models import StockTakingTimes, TimeStamp

class TimeStampIDSerializer(serializers.ModelSerializer):

    # productid = serializers.StringRelatedField()
    # container = serializers.StringRelatedField(source='containernameid')

    class Meta:
        model = TimeStamp
        fields = '__all__'