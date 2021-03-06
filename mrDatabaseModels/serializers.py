from rest_framework import serializers
from .models import Productlist, ProcessedStockAmounts, StockTakingTimes, Productcontainers, Productcontainernames, TimeStamp, MeatriteStock


# This serializer is made to give a list through of all the products that we have
class ProductListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # description = serializers.CharField(source='proddescription')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='brand')
    packaging = serializers.SlugRelatedField(read_only=True, slug_field='packaging_type')
    # batchgroup = serializers.SlugRelatedField(read_only=True, slug_field='batchname')
    batchgroup = serializers.StringRelatedField(source='stocktakegroup')
    description = serializers.CharField(source='proddescription')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        # Then name of the model that you want to serialize (Remember to import the model)
        model = Productlist
        # All the fields that you want to show/work with
        fields = ('brand', 'packaging', 'unitweight', 'productid', 'batchgroup', 'description')
        # All the field that you want to be read only (Can not be changed)
        read_only_fields = ('batchranking',)



class ProcessedStockSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='prodName')
    container = serializers.SlugRelatedField(read_only=True, slug_field='containername')

    class Meta:
        model = ProcessedStockAmounts
        fields = ('name','amount','container')


# ----------------------------------------------------------------------------


class ReturnContainers(serializers.ModelSerializer):
    # containernameid = serializers.SlugRelatedField(read_only=False, slug_field='containerName', queryset=Productcontainernames.objects.all())
    containernameid = serializers.SlugRelatedField(read_only=False, slug_field='containername', queryset=Productcontainernames.objects.all())
    productid = serializers.SlugRelatedField(read_only=False, slug_field='productid', queryset=Productlist.objects.all())
    class Meta:
        model = Productcontainers
        # fields = ('productid','containernameid')
        fields = ('productid','containernameid')

class ProcessedStockSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Productcontainers
        fields = '__all__'

# ----------------------------------------------------------------------------

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productlist
        fields = ('productid',)

class TestSerializer(serializers.ModelSerializer):
    
    time = serializers.SlugRelatedField(read_only=False, slug_field='times', queryset=StockTakingTimes.objects.all())
    prodName = serializers.SlugRelatedField(read_only=False, slug_field='productid', queryset=Productlist.objects.all())
    container = serializers.SlugRelatedField(read_only=False, slug_field='containername', queryset=Productcontainernames.objects.all())

    class Meta:
        model = ProcessedStockAmounts
        fields = ('prodName','amount','time', 'container')

class ProductContainersSerializer(serializers.ModelSerializer):

    productid = serializers.StringRelatedField()
    container = serializers.StringRelatedField(source='containernameid')

    class Meta:
        model = Productcontainers
        fields = ('id', 'productid', 'container', 'deleteContainerAmount')

# ----------------------------------------------------------------------------

class GetStockTimesSerializer(serializers.ModelSerializer):

    times = serializers.StringRelatedField()

    class Meta:
        model = StockTakingTimes
        fields = ('times',)



class ProcessedStockAmountsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProcessedStockAmounts
        fields = ('prodName','amount','time','container')

class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields = '__all__'

class MeatriteStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeatriteStock
        fields = '__all__'