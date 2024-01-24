from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

from user.serializers import RegisterSerializer,UserSerializer
from user.models import User

class RegisterViewSet(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []


    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if serializer.is_valid():

            user = User.objects.create(**serializer.data)
            user.set_password(serializer.data['password'])
            user.is_active = True
            user.save()
            data = serializer.data
            data['id'] = user.id
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.filter()

    def get_serializer_class(self):
        serializer_mapping = {
            # 'POST': ProfileCreateSerializer,
            # 'PATCH': ProfilePatchSerializer,
            'GET': UserSerializer
        }
        method = self.request.method
        return serializer_mapping.get(method, UserSerializer)
    
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
# from .models import User
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated

# @api_view(['POST'])
# @csrf_exempt
# permission_classes = [AllowAny]
# authentication_classes = []
# def userdetail(request):
#     try:
#         # Assuming the token is passed in the request's Authorization header
#         token = request.headers['Authorization'].split(' ')[1]
#         user = User.objects.get(auth_token__key=token)
#         user = User.objects.get(email=user.email)

#         user_details = {
#             'email': user.email,
#             'level': user.level,
#             # Add other fields as needed
#         }

#         return JsonResponse(user_details)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)