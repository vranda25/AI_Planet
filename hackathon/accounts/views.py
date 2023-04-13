from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

# Register 
class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = CustomUserSerializer(data=data)
            print('0............')
            if serializer.is_valid():
                print('1............')
                user = CustomUser.objects.create_user(email=serializer.data['email'], password=serializer.data['password'], first_name=serializer.data['first_name'], last_name=serializer.data['last_name'])
                user.save()
                print('2............')
                return Response({
                    'status': 200,
                    'message': 'Registration successfull!!',
                    'data': serializer.data.get('email'),
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e, '______________________________')
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': {},
            })


# Login using email and password
class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']

                user = authenticate(email=email, password=password)
                print(email)
                print(password)
                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid mail or password',
                        'data': serializer.errors,
                    })

                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': 'Success!',
                    'message': 'Welcome',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
               })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': {},
            })

