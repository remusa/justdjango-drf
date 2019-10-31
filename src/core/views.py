from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.all()
        post = all_posts.first()
        # serializer = PostSerializer(all_posts, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# def test_view(APIView):
#     data = {"name": "john", "age": 23}
#     return JsonResponse(data)
