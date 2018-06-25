from rest_framework import serializers
from .models import Productlist


# This serializer is made to give a list through of all the products that we have
class ProductListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # description = serializers.CharField(source='proddescription')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='brand')
    packaging = serializers.SlugRelatedField(read_only=True, slug_field='packagingType')
    batchgroup = serializers.SlugRelatedField(read_only=True, slug_field='batchname')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        # Then name of the model that you want to serialize (Remember to import the model)
        model = Productlist
        # All the fields that you want to show/work with
        fields = ('brand', 'packaging', 'unitweight', 'productid','batchgroup')
        # All the field that you want to be read only (Can not be changed)
        read_only_fields = ('batchranking',)
