from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.response import Response
from redis_app.models import TableA, TableB, TableC, TableD, TableE
from redis_app.serializers import (TableASerializer, 
    TableBSerializer, TableCSerializer, TableDSerializer, TableESerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60*2)


# Create your views here.

class GeneralPagination(PageNumberPagination):
    page_size = 5000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClearCache(APIView):
    def get(self, request, *args, **kwargs):
        cache.clear()
        return Response({"Message": "Cache Cleared"})


class TableAView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = TableA.objects.all().order_by('id')
    serializer_class = TableASerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TableBView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = TableB.objects.all().order_by('id')
    serializer_class = TableBSerializer


    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TableCView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = TableC.objects.all().order_by('id')
    serializer_class = TableCSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TableDView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = TableD.objects.all().order_by('id')
    serializer_class = TableDSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TableEView(viewsets.ModelViewSet):
    pagination_class = GeneralPagination
    queryset = TableE.objects.all().order_by('id')
    serializer_class = TableESerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

