

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if not book.borrowed:
        book.borrowed = True
        book.save()
    return redirect('book_list')

def return_book(request, id):
    book = Book.objects.get(id=id)
    if book.borrowed:
        book.borrowed = False
        book.save()
    return redirect('book_list')


