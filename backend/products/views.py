from django.shortcuts import render
from requests import request
from api.permissions import IsStaffEditorPermission
from api.mixins import IsStaffUserPermissionMixin, UserQuerySetMixin
from rest_framework import generics, permissions, authentication

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListCreateAPIView(UserQuerySetMixin ,IsStaffUserPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(content=content, user= self.request.user)

    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     qs = super().get_queryset() # --> product.objects.all()

    #     return qs.filter(user=user)
        

    
class ProductCreateApiView(IsStaffUserPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None


        if content is None:
            content = title
        
        serializer.save(content=content)

class ProductDetailAPIView(IsStaffUserPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductUpdateAPIView(IsStaffUserPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    def perform_update(self, serializer):
        instance = serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        price = serializer.validated_data.get('price')

        if not instance.content:
            instance.content = instance.title
        

class ProductDeleteAPIView(IsStaffUserPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

