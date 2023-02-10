from django.urls import path

from . import views

urlpatterns=[
    
    path('', views.ProductListCreateAPIView.as_view()),
    path('create/', views.ProductCreateApiView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update-product/', views.ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete-product/', views.ProductDeleteAPIView.as_view())
]