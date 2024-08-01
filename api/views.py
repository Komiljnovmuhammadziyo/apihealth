from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from api import serializers
from api.serializers import UserDetailSerializer
from users.models import CustomUser




class UserListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = CustomUser.objects.all().order_by('email')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(queryset, request)

        serializer = UserDetailSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)

    def login(self, request):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIVIew(APIView):
    def get(self, request, id):
        queryset = CustomUser.objects.get(id = id)
        serializer = UserDetailSerializer(queryset)

        return Response(serializer.data)

    def logout(self, request, id):
        queryset = CustomUser.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def update(self, request, id):
        queryset = CustomUser.objects.get(id=id)
        serializer = UserDetailSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
