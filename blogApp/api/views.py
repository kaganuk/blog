from blogApp.models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        """Receives post request and returns saved post data."""
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid()
        serializer.save(author=request.user)
        return Response(serializer.data)
