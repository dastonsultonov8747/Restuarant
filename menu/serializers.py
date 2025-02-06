from .models import BigMenu, SmallMenu, Product
from rest_framework import serializers


class BigMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigMenu
        fields = '__all__'  # Barcha maydonlarni qo'shish


class SmallMenuSerializer(serializers.ModelSerializer):
    bigmenu = BigMenuSerializer()  # BigMenu haqida to'liq ma'lumot olish

    class Meta:
        model = SmallMenu
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    smallmenu = SmallMenuSerializer()  # SmallMenu haqida to'liq ma'lumot olish

    class Meta:
        model = Product
        fields = '__all__'