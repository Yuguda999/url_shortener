from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortURL
from .serializers import ShortURLSerializer, ShortURLCreateSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CreateShortURL(APIView):
    @swagger_auto_schema(
        request_body=ShortURLCreateSerializer,
        responses={201: ShortURLSerializer, 400: 'Bad Request'},
        operation_description="Create a new short URL."
    )
    def post(self, request):
        serializer = ShortURLCreateSerializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.save()
            return Response(ShortURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveOriginalURL(APIView):
    @swagger_auto_schema(
        responses={200: ShortURLSerializer, 404: 'Not Found'},
        operation_description="Retrieve the original URL from a short URL."
    )
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.access_count += 1
        short_url.save()
        return Response(ShortURLSerializer(short_url).data, status=status.HTTP_200_OK)

class UpdateShortURL(APIView):
    @swagger_auto_schema(
        request_body=ShortURLCreateSerializer,
        responses={200: ShortURLSerializer, 400: 'Bad Request', 404: 'Not Found'},
        operation_description="Update an existing short URL."
    )
    def put(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLCreateSerializer(short_url, data=request.data)
        if serializer.is_valid():
            updated_short_url = serializer.save()
            return Response(ShortURLSerializer(updated_short_url).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteShortURL(APIView):
    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'},
        operation_description="Delete an existing short URL."
    )
    def delete(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class URLStats(APIView):
    @swagger_auto_schema(
        responses={200: ShortURLSerializer, 404: 'Not Found'},
        operation_description="Get statistics for a short URL, including the number of times it was accessed."
    )
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return Response(ShortURLSerializer(short_url).data, status=status.HTTP_200_OK)
