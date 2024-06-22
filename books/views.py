from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from books.models import BookModel
from books.serializers import BookSerializer
from rest_framework import generics
from rest_framework.views import APIView


# @api_view(['GET'])
# def get_all_books(request, *args, **kwargs):
#     books = BookModel.objects.all()
#     data = BookSerializer(books, many=True).data
#     return Response(data)

# class BookListAPIView(generics.ListAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        response = {
            'success': True,
            'total': books.count(),
            'books': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def get_book(request, pk, *args, **kwargs):
#     try:
#         book = BookModel.objects.get(pk=pk)
#     except BookModel.DoesNotExist:
#         return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#     data = BookSerializer(book).data
#     return Response(data)

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookSerializer(book)
        response = {
            'success': True,
            'book': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


# @api_view(['PUT'])
# def update_book_view(request, pk, *args, **kwargs):
#     try:
#         book = BookModel.objects.get(pk=pk)
#     except BookModel.DoesNotExist:
#         return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     serializer = BookSerializer(book, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book updated',
                'book': serializer.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def update_book_view(request, pk, *args, **kwargs):
#     try:
#         book = BookModel.objects.get(pk=pk)
#     except BookModel.DoesNotExist:
#         return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#     serializer = BookSerializer(book, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def create_book_view(request, *args, **kwargs):
#     data = request.data
#     serializer = BookSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)





# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


class BookCreateAPIView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book is created',
                'book': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_book_book(request, pk, *args, **kwargs):
#     try:
#         book = BookModel.objects.get(pk=pk)
#     except BookModel.DoesNotExist:
#         return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#     book.delete()
#     return Response({'message': 'Book is deleted'}, status=status.HTTP_204_NO_CONTENT)

# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializer


class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        book.delete()
        response = {
            'success': True,
            'message': 'Book is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
