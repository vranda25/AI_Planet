from .serializer import *
from accounts.models import CustomUser
from accounts.serializer import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# Create hackathon
class CreateHackView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            print('12----------------')
            data = request.data
            serializer = CreateHackSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Hackathon has been created successfully!',
                    'data': serializer.data,
                })
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': {'error': str(e)}
            })


# List all hackathons
class ListHacksView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            print('..............')
            queryset_hacks = CreateHack.objects.all()
            print('here')
            serialize = CreateHackSerializer(queryset_hacks, many=True)
            print('done')
            return Response({
                'status': '200',
                'data': serialize.data
            })
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': {'error': str(e)}
            })
