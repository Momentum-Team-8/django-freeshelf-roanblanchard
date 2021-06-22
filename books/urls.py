from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("books/", views.book_list, name="book_list")
]