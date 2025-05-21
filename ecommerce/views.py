from django.shortcuts import render
from rest_framework import generics
from .serializers import ProdutosSerializer
from .models import Produtos
from .permissions import AutenticadoOuApenasLeitura
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProdutosFilter
# Create your views here.


class ProdutoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [AutenticadoOuApenasLeitura]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutosFilter

class ProdutoUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [AutenticadoOuApenasLeitura]
