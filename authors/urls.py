from django.url import path

from authors.views import *

urlpatterns = [
    path('', AuthorListAPIView.as_view()),
    path('create/', AuthorCreateAPIView.as_view()),
    path('<int:pk>/', AuthorDetailAPIView.as_view()),
    path('<int:pk>/update/', AuthorUpdateAPIView.as_view()),
    path('<int:pk>/patch/', AuthorUpdateAPIView.as_view()),
    path('<int:pk>/delete/', AuthorDeleteAPIView.as_view()),
]