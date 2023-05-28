from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new user with data sent in post request'
        },
    ]
    return Response(routes)



@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = make_password(request.data.get('password'))

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email, password=password)
    return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    print(f"Username: {username}")
    print(f"Password: {password}")

    user = authenticate(username=username, password=password)

    if user is not None:
        stored_password = user.password
        if check_password(password, stored_password):
            login(request, user)
            print("Authentication successful")
            return Response({'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)
        else:
            print("Stored Password:", stored_password)
            print("Authentication failed: Password mismatch")
    else:
        print("Authentication failed: User not found")

    return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


