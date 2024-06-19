from django.urls import path, include
from .views import UserLoginView, SignUpView

from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', SignUpView.as_view({'post': 'create'}), name='signup'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login'),
    path('', include(router.urls)),

]
