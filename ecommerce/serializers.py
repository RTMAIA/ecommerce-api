from rest_framework import serializers
from .models import Produtos


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

    def validate_preco(self, value):
        if value <= 0: 
            raise serializers.ValidationError('A preço não poder ser igual ou menor que zero.')
        return value
    
    def validate_quantidade_estoque(self, value):
        if value <= 0:
            raise serializers.ValidationError('A quantidade de estoque não pode ser igual ou menor que zero.')
        return value