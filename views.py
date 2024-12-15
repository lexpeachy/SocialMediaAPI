# views.py
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=400)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User registered successfully", "user_id": user.id}, status=201)

@api_view(['GET'])
def fetch_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
