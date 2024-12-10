from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return JsonResponse({"books": list(books.values())})