from django.urls import path,include
from user.views import RegisterViewSet,UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)
# from .views import userdetail
router = routers.DefaultRouter()
router.register(
        r'',
        UserViewSet,
        basename='users'
    )

urlpatterns = [
    
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    # path('details/', userdetail, name='user-detail'),
    path('', include(router.urls)),
    
]