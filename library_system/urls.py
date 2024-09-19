from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:id>/', views.return_book, name='return_book'),
]
