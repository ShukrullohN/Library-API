from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from authors.models import AuthorModel
from authors.serializers import AuthorSerializer
from rest_framework import generics
from rest_framework.views import APIView



class AuthorListAPIView(APIView):
    def get(self, request):
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        response = {
            'success': True,
            'total': authors.count(),
            'authors': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)




class AuthorDetailAPIView(APIView):
    def get(self, request, pk):
        author = get_object_or_404(AuthorModel, pk=pk)
        serializer = AuthorSerializer(author)
        response = {
            'success': True,
            'author': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)





class AuthorUpdateAPIView(APIView):
    def put(self, request, pk):
        author = get_object_or_404(AuthorModel, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Author updated',
                'author': serializer.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)






class AuthorCreateAPIView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Author is created',
                'author': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class AuthorDeleteAPIView(APIView):
    def delete(self, request, pk):
        author = get_object_or_404(AuthorModel, pk=pk)
        author.delete()
        response = {
            'success': True,
            'message': 'Author is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
