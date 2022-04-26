# from rest_framework import views as api_views
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics as api_views

from django_rest_framework.api.models import Product, Category


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = IdAndNameCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class CategoriesListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class ProductsListView(api_views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
