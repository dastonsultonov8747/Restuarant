from .models import BigMenu, SmallMenu, Product, Aksiya, Slider, NewProduct, Order
import random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BigMenuSerializer, SmallMenuSerializer, ProductSerializer
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    bigmenus = BigMenu.objects.all()
    product = Product.objects.all()
    random_list = random.sample(list(product), min(len(product), 7))
    aksiya = Aksiya.objects.all()
    news_foods = NewProduct.objects.all()
    sliders = Slider.objects.all()
    ctg = {
        'bigmenus': bigmenus,
        'aksiya': aksiya,
        'news_foods': news_foods,
        'random_list': random_list,
        'sliders': sliders
    }
    return render(request, 'index.html', ctg)


def about(request):
    return render(request, 'about-us.html')


def menu(request):
    return render(request, 'food_menus.html')


# BigMenu API
class BigMenuListView(APIView):
    def get(self, request):
        bigmenus = BigMenu.objects.all()
        serializer = BigMenuSerializer(bigmenus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BigMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BigMenuDetailView(APIView):
    def get_object(self, pk):
        try:
            return BigMenu.objects.get(pk=pk)
        except BigMenu.DoesNotExist:
            return None

    def get(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BigMenuSerializer(bigmenu)
        return Response(serializer.data)

    def put(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BigMenuSerializer(bigmenu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        bigmenu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SmallMenu API
class SmallMenuListView(APIView):
    def get(self, request):
        smallmenus = SmallMenu.objects.all()
        serializer = SmallMenuSerializer(smallmenus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SmallMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmallMenuDetailView(APIView):
    def get_object(self, pk):
        try:
            return SmallMenu.objects.get(pk=pk)
        except SmallMenu.DoesNotExist:
            return None

    def get(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SmallMenuSerializer(smallmenu)
        return Response(serializer.data)

    def put(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SmallMenuSerializer(smallmenu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        smallmenu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Product API
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
