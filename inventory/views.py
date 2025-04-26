# inventory/views.py
from django.shortcuts import render
from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Supplier, Item
from django.db.models import F, Sum, Avg
from .serializers import CategorySerializer, SupplierSerializer, ItemSerializer

# ================== CATEGORIES ==================

# Viewset untuk Category (API)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ================== SUPPLIERS ==================

# Viewset untuk Supplier (API)
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# ================== ITEMS ==================

# Viewset untuk Item (API)
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Override the update method to handle item edit
    def update(self, request, *args, **kwargs):
        item = self.get_object()  # Ambil objek item yang akan diedit
        serializer = self.get_serializer(item, data=request.data, partial=True)  # Data parsial agar hanya field yang diubah
        if serializer.is_valid():
            serializer.save()  # Simpan perubahan
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Override the destroy method to handle item delete
    def destroy(self, request, *args, **kwargs):
        item = self.get_object()  # Ambil objek item yang akan dihapus
        item.delete()  # Hapus item
        return Response(status=status.HTTP_204_NO_CONTENT)  # Response kosong setelah penghapusan

# ================== Web Views ==================

# Fungsi untuk menampilkan daftar item (Web)
def items_list(request):
    items = Item.objects.all()  # Ambil semua item
    return render(request, 'inventory/items_list.html', {'items': items})

# Fungsi untuk menampilkan ringkasan stok barang
def stock_summary(request):
    items = Item.objects.all()
    total_quantity = items.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_value = items.aggregate(total=Sum(F('quantity') * F('price')))['total'] or 0
    avg_price = total_value / total_quantity if total_quantity > 0 else 0
    

    threshold = 5
    low_stock_items = items.filter(quantity__lt=threshold)

    context = {
        'total_quantity': total_quantity,
        'total_value': total_value,
        'avg_price': avg_price,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'inventory/stock_summary.html', context)

# Fungsi untuk menampilkan barang dengan stok rendah
def low_stock_items(request):
    threshold = 5
    low_stock_items = Item.objects.filter(quantity__lt=threshold)

    context = {
        'low_stock_items': low_stock_items,
    }
    return render(request, 'inventory/low_stock_items.html', context)

# Fungsi untuk menambahkan item baru (Web)
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        supplier_id = request.POST.get('supplier')
        quantity = request.POST.get('quantity')

        raw_price = request.POST.get('price')
        cleaned_price = int(raw_price.replace('.', '').replace(',', ''))

        category = Category.objects.get(id=category_id)
        supplier = Supplier.objects.get(id=supplier_id)

        new_item = Item(
            name=name, 
            category=category, 
            supplier=supplier, 
            quantity=quantity, 
            price=cleaned_price
        )
        new_item.save()

        return redirect('items_list')

    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/add_item.html', {'categories': categories, 'suppliers': suppliers})

# Fungsi untuk mengedit item (Web)
def edit_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.category = Category.objects.get(id=request.POST.get('category'))
        item.supplier = Supplier.objects.get(id=request.POST.get('supplier'))
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.save()

        return redirect('items_list')

    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/edit_item.html', {'item': item, 'categories': categories, 'suppliers': suppliers})

# Fungsi untuk menghapus item (Web)
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('items_list')

# Fungsi untuk menampilkan daftar kategori (Web)
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'inventory/categories_list.html', {'categories': categories})

# Fungsi untuk menambahkan kategori baru (Web)
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('categories_list')
    return render(request, 'inventory/add_category.html')

# Fungsi untuk menampilkan daftar supplier (Web)
def suppliers_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/suppliers_list.html', {'suppliers': suppliers})

# Fungsi untuk menambahkan supplier baru (Web)
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
    
        if name:
            Supplier.objects.create(name=name, contact_info=contact_info)
            return redirect('suppliers_list')
    return render(request, 'inventory/add_supplier.html')
