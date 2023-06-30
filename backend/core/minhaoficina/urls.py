from django.urls import include, path
from rest_framework import routers
from minhaoficina.views import OficinaViewSet, ClienteViewSet, VeiculoViewSet, ServicoViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'oficinas', OficinaViewSet, basename='oficina')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'veiculos', VeiculoViewSet, basename='veiculo')
router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
]