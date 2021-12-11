from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from registerApp.views import VerifyTokenView, UserCreateView, UserDetailView
from mediopagoApp.views import MedioCreateView, MedioListView, MedioDeleteView, MedioUpdateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', VerifyTokenView.as_view()),
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('mediopago/create/<int:pk>/', MedioCreateView.as_view()),
    path('mediopago/<int:pk>/', MedioListView.as_view()),
    path('mediopago/delete/<int:pk>/',MedioDeleteView.as_view()),
    path('mediopago/update/<int:pk>/', MedioUpdateView.as_view())
]
