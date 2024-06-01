from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, DataViewSet, AlertViewSet
from .views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'data', DataViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
