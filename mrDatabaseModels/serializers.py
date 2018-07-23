from rest_framework import serializers
from .models import Productlist, ProcessedStockAmounts, StockTakingTimes, Productcontainers, Productcontainernames


# This serializer is made to give a list through of all the products that we have
class ProductListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # description = serializers.CharField(source='proddescription')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='brand')
    packaging = serializers.SlugRelatedField(read_only=True, slug_field='packaging_type')
    batchgroup = serializers.SlugRelatedField(read_only=True, slug_field='batchname')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        # Then name of the model that you want to serialize (Remember to import the model)
        model = Productlist
        # All the fields that you want to show/work with
        fields = ('brand', 'packaging', 'unitweight', 'productid','batchgroup')
        # All the field that you want to be read only (Can not be changed)
        read_only_fields = ('batchranking',)



class ProcessedStockSerializer(serializers.ModelSerializer):
    # prodName = serializers.SlugRelatedField(read_only=True, slug_field='productid', required=False)
    name = serializers.CharField(source='prodName')
    # time = serializers.SlugRelatedField(read_only=True, slug_field='times')

    class Meta:
        model = ProcessedStockAmounts
        fields = '__all__'
        #fields = ('name', 'amount')

    def to_representation(self, instance):
        result = super(ProcessedStockSerializer, self).to_representation(instance)
        new_result = {result['name']: result['amount']}
        return new_result

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
    # prodName = serializers.CharField()
    # prodName = ProductSerializer(many=True, read_only=True)
    prodName = serializers.SlugRelatedField(read_only=False, slug_field='productid', queryset=Productlist.objects.all())
    # prodName = ProductSerializer(many = True)
    # prodName = serializers.SlugRelatedField(read_only=True, slug_field='prodName')

    class Meta:
        model = ProcessedStockAmounts
        fields = ('prodName','amount','time')
