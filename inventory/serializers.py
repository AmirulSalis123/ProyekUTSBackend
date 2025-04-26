from rest_framework import serializers
from .models import Category, Supplier, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    supplier = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'supplier', 'quantity', 'price', 'added_by']

