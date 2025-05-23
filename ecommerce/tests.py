from rest_framework.test import APITestCase
from .models import Produtos
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# Create your tests here.

class ProdutoAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='rafael', password='rafael')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.produto = Produtos.objects.create(
            nome = 'Cadeira Gamer',
            descricao = 'Cadeira Gamer Bacana Demais',
            quantidade_estoque = 10,
            preco = 1200
        )

    def test_listar_produtos(self):
        url = reverse('produto_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


    def test_criar_produto(self):
        url = reverse('produto_list')
        data = {
            "nome": "Suporte para monitor",
            "descricao": "Suporta para monitor tipo VERSA",
            "quantidade_estoque": 10,
            "preco": 169.00
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], "Suporte para monitor")


    def test_detalhar_produto(self):
        url = reverse('produto_retrieve', kwargs={'pk': self.produto.pk})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.produto.nome)


    def test_atualizar_produto(self):
        url = reverse('produto_retrieve', kwargs={'pk': self.produto.pk})
        data = {
            "nome": "Suporte para dois monitores",
            "descricao": "Suporte para dois monitores tipo VERSA",
            "quantidade_estoque": 10,
            "preco": 269.00
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], data['nome'])
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, data['nome'])


    def test_deletar_produto(self):
        url = reverse('produto_retrieve', kwargs={'pk': self.produto.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Produtos.objects.filter(pk=self.produto.pk).exists())


    def test_erro_criar_produto_sem_nome(self):
        url = reverse('produto_list')
        data = {
            "descricao": "teste sem nome",
            "quantidade_estoque": 10,
            "preco": 269.00
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('nome', response.data)