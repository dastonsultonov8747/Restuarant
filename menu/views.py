from .models import BigMenu, SmallMenu, Product, Aksiya, Slider, NewProduct, Tables, Order
import random
from rest_framework.response import Response
from rest_framework import status
from .forms import PeopleOrderForm
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


#
# def contacts_view(request):
#     tables = Tables.objects.all()
#     if request.method == 'POST':
#         form = PeopleOrderForm(request.POST)
#         print("////////////////////////////////////////////////////////////////////////")
#         if form.is_valid():
#             # Formadagi ma'lumotlarni o'zgaruvchiga olish
#             name = request.POST.get('name')
#             surname = request.POST.get('surname')
#             email = request.POST.get('email')
#             phone = request.POST.get('phone')
#             table = request.POST.get('table')
#             buyurma_sanasi = request.POST.get('buyurma_sanasi')
#             mehmonlar_soni = request.POST.get('mehmonlar_soni')
#             maxsus_sorovlar = request.POST.get('maxsus_sorovlar')
#
#             # Yangi model obyektini yaratish va saqlash
#             new_order = Order(
#                 name=name,
#                 surname=surname,
#                 email=email,
#                 phone=phone,
#                 table=table,
#                 buyurma_sanasi=buyurma_sanasi,
#                 mehmonlar_soni=mehmonlar_soni,
#                 maxsus_sorovlar=maxsus_sorovlar
#             )
#             print("////////////////")
#             print("malumotlar qabul qilindi")
#             new_order.save()
#             return redirect('/')
#     else:
#         form = PeopleOrderForm()
#
#     return render(request, 'contacts.html', {'form': form, 'tables': tables})


def contacts_view(request):
    tables = Tables.objects.all()
    if request.method == 'POST':
        # POST metodini ishlatishda ma'lumotlarni olish
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        tel = request.POST.get('phone')
        table = request.POST.get('mehmonlar_soni')
        kimbn = request.POST.get('kim_bn')
        buyurma_sanasi = request.POST.get('buyurma_sanasi')
        maxsus_sorovlar = request.POST.get('maxsus_sorovlar')
        new_order = Order(
            ismi=name,
            fmiliasi=surname,
            email=email,
            tel=tel,
            table=table,
            kim_bn=kimbn,
            buyurma_sanasi=buyurma_sanasi,
            maxsus_sorovlar=maxsus_sorovlar
        )
        new_order.save()
        return redirect('/')
    else:
        return render(request, 'contacts.html', {'tables': tables})


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
