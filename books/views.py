from django.shortcuts import render
from .models import Book, Category
from django.utils import timezone

# Create your views here.


def homepage(request):
    return render(request, "books/homepage.html")

def book_list(request):
    books = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'books/book_list.html', {'books': books})

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.albums.all()

    return render(request, "books/show_category.html", {"category": category, "books": books})