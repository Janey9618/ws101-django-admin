# product/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),  # Product list URL
    path('create/', views.product_create, name='product_create'),  # Product create URL
    path('<int:pk>/update/', views.product_update, name='product_update'),  # Product update URL
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),  # Product delete URL
]
