from .serializer import *
from accounts.models import CustomUser
from accounts.serializer import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# Regiter to a particular hackathon, hackathon id required
class RegisterHackView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            print('12----------------')
            user = request.user
            hackathon = request.data.get('hackathon')
            print('..................')
            data = {'user': user.id, 'hackathon' : hackathon}
            print('*')
            serializer = RegisterHackSerializer(data=data)
            print('vvvvvvvvvvvv')
            if serializer.is_valid():
                print('oooooooooooooooooo')
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Resgistration for successfull!',
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


# List of all registered hackathons by a user
class ListAllRegisteredHacksView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            print('12----------------')
            user = request.user
            queryset_registered = ResigterHack.objects.filter(user=user)
            serializer = RegisterHackSerializer(queryset_registered, many=True)
            return Response({
                'status': 200,
                'message': 'List of registered hackathons',
                'data': serializer.data,
            })
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': {'error': str(e)}
            })


# Submission of Registered hackathon
class UploadSubmissionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            registered_hack = request.data.get('registered_hack')
            print(registered_hack)
            hackathon = registered_hack.objects.get('hackathon')
            print(hackathon)
            registered_hack = {'registered_hack' : registered_hack}
            data = request.data
            data = {**data, **registered_hack}
            serializer = UploadSubmissionSerializer(data=data)
            print('here')
            if serializer.is_valid():
                print('there')
                
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Successful submission!',
                    'data': serializer.data,
                })
            return Response({
                'status': '400',
                'message': 'Service is not completed:|',
                'data': serializer.errors,
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': {'error': str(e)}
            })


# List of Submissions of all hackathons by a user
class ListSubmissionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user = request.user
            query_register = ResigterHack.objects.filter(user=user)
            serializer_register = RegisterHackSerializer(query_register, many=True)
            print(serializer_register.data)

            register = []
            registered_hacks = []
            for i in serializer_register.data:
                register.append(i.get('id'))
                registered_hacks.append(i.get('hackathon'))
            print(register)
            print(registered_hacks)

            submission = []
            for i in register:
                query_submission = UploadSubmission.objects.filter(registered_hack=i)
                serializer_submission = UploadSubmissionSerializer(query_submission, many=True)
                print(serializer_submission.data)
                if len(serializer_submission.data) > 0:
                    submission.append(serializer_submission.data[0])

            return Response({
                'status': 200,
                'message': 'Rating',
                'data': submission,
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status': '400',
                'message': 'Something went wrong',
                'data': {'error': str(e)}
            })


