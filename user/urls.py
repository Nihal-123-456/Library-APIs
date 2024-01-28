from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('list',UserView)
router.register('wishlist',WishlistView)
router.register('borrowhistory',BorrowHistoryView)

urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegistrationView.as_view(), name='register'),
    path('active/<uid64>/<token>',activate,name='active'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]