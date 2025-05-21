from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtein_pair'),
    path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),


    path('produtos/', views.ProdutoListCreateAPIView.as_view(), name='produto_list'),
    path('produtos/<int:pk>', views.ProdutoUpdateDestroyAPIView.as_view(), name='produto_retrieve')
]
