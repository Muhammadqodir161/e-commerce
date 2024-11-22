from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='list'),
    path('book/detail/<int:pk>/', views.book_detail, name='detail'),
    path('book/create/', views.create_book, name='create'),
    path('book/update/<int:pk>/', views.update_book, name='update'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete'),
]
