from django.urls import path
from .views import UserLoginView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view({'post': 'create'}), name='signup'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login')
]
