from asyncore import read
from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import validate_title
from .validators import unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    pk =  serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField()
    detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators=[validate_title, unique_product_title])
    class Meta:
        model = Product
        fields = [
            'pk',
            'user',
            'edit_url',
            'detail_url',
            'title',
            'content',
            'price',
            'new_price',
            'discount'
        ]

    def get_user(self, obj):
        return obj.user.username
    def get_edit_url(self, obj):
        request =  self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk':obj.pk}, request=request)

    def get_pk(self, obj):
        return obj.pk

    def get_discount(self, obj):
        # obj --> (model)Product instance
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_product_discount()
    