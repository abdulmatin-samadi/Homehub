"""properties app uchun URL marshrutlari (to'liq CRUD)."""
from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property_list'),
    path('qoshish/', views.PropertyCreateView.as_view(), name='property_create'),
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('<int:pk>/tahrirlash/', views.PropertyUpdateView.as_view(), name='property_update'),
    path('<int:pk>/ochirish/', views.PropertyDeleteView.as_view(), name='property_delete'),
]
