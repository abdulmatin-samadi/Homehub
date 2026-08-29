"""chat app uchun URL marshrutlari."""
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.conversation_list_view, name='conversation_list'),
    path('boshlash/<int:property_pk>/', views.start_conversation_view, name='start_conversation'),
    path('<int:pk>/', views.conversation_detail_view, name='conversation_detail'),
]
