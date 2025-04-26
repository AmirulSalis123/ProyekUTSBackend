from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Impor semua views di sini

# Router untuk API endpoint
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    # ---------- Web Views ----------

    # Items
    path('items/', views.items_list, name='items_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/edit/<int:id>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:id>/', views.delete_item, name='delete_item'),

    # Categories (Create + Read)
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/add/', views.add_category, name='add_category'),

    # Suppliers (Create + Read)
    path('suppliers/', views.suppliers_list, name='suppliers_list'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),

    # ---------- Additional Web Views ----------
    
    # Stock Summary
    path('stock-summary/', views.stock_summary, name='stock_summary'),

    # Low Stock Items (stok dibawah ambang batas)
    path('low-stock-items/', views.low_stock_items, name='low_stock_items'),

    # ---------- API Routes ----------
    path('api/', include(router.urls)),
]
