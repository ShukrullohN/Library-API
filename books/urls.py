from django.url import path

from books.views import *

urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('create/', BookCreateAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
    path('<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('<int:pk>/patch/', BookUpdateAPIView.as_view()),
    path('<int:pk>/delete/', BookDeleteAPIView.as_view()),
]