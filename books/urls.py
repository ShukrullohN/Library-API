
from django.urls import path

from books.views import get_all_books, get_book, update_book_view, create_book_view, delete_book_book

urlpatterns = [
    path('', get_all_books),
    path('create/', create_book_view),
    path('<int:pk>/', get_book),
    path('<int:pk>/update/', update_book_view),
    path('<int:pk>/delete/', delete_book_book),
]