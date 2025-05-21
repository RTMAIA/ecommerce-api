import django_filters
from .models import Produtos


class ProdutosFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    preco_min = django_filters.NumberFilter(field_name='preco', lookup_expr='gte')
    preco_max = django_filters.NumberFilter(field_name='preco', lookup_expr='lte')
    class Meta:
        model = Produtos
        fields = ['nome', 'preco_min', 'preco_max']