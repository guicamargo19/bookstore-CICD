# type: ignore
from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")


"""     def get_queryset(self):
        return Category.objects.all().order_by("id") """
