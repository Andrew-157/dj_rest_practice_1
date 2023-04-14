from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.username')

    class Meta:
        model = Product
        fields = ['id', 'title', 'description',
                  'category', 'unit_price', 'vendor']
