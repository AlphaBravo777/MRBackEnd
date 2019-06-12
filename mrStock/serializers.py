from rest_framework import serializers
from mrDatabaseModels.models import ProcessedStockAmounts
from .models import HPPMeatriteStock, HPPProductStatus

class CreateOrUpdateProcStockSerializer(serializers.ModelSerializer):

    # productid = serializers.StringRelatedField()
    # container = serializers.StringRelatedField(source='containernameid')

    class Meta:
        model = ProcessedStockAmounts
        fields = '__all__'
        # fields = ('id', 'productid', 'container', 'deleteContainerAmount')

class HPPMeatriteStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = HPPMeatriteStock
        fields = '__all__'        