from django.shortcuts import render
from .models import Book
from django.utils import timezone

# Create your views here.


def book_list(request):
    book = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'books/book_list.html', {'book': book})