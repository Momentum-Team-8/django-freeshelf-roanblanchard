from django.shortcuts import render
from .models import Book
from django.utils import timezone

# Create your views here.


def homepage(request):
    return render(request, "books/homepage.html")

def book_list(request):
    books = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'books/book_list.html', {'books': books})