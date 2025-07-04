from rest_framework.views import APIView
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
class CorePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductListAPIView(APIView):
    """
    GET /api/products/

    Retrieve a paginated list of products.

    Query Parameters:
    - category (str): Filter products by category name (case-insensitive).
        e.g. `/api/products/?category=Electronics`
    - search (str): Search products by name or description (case-insensitive).
        e.g. `/api/products/?search=laptop`
    - ordering (str): Order by 'price' or 'name'. Prefix with '-' for descending order.
        e.g. `/api/products/?ordering=price`, `/api/products/?ordering=-name`
    - page (int): Page number for pagination.
        e.g. `/api/products/?page=2`
    - page_size (int): Number of items per page (max 100).
        e.g. `/api/products/?page_size=20`

    Example:
    `/api/products/?category=Electronics&search=phone&ordering=-price&page=1&page_size=10`
    """

    pagination_class = CorePagination
    @method_decorator(ratelimit(key='user_or_ip', rate='10/m', method='GET', block=True))
    def get(self, request):
        
        queryset = Product.objects.all()

        # Filter by category name (case-insensitive)
        category_name = request.query_params.get('category')
        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)

        # Search in name or description
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        # Ordering
        ordering = request.query_params.get('ordering')
        if ordering in ['price', '-price', 'name', '-name']:
            queryset = queryset.order_by(ordering)

        # Paginate and serialize
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = ProductSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


