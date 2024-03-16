from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer
from . import swagger as sw


# Create your views here.
class RegistrationView(APIView):
    @swagger_auto_schema(
        operation_id='User Register',
        operation_description='User Register',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': sw.ums_email,
                'password': sw.ums_password,
                'gender': sw.ums_gender
            },
            required=['email', 'password']
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'id': sw.ums_id,
                        'password': sw.ums_password,
                        'email': sw.ums_email,
                        'name': sw.ums_name,
                        'gender': sw.ums_gender,
                        'is_staff': sw.ums_is_staff,
                        'is_superuser': sw.ums_is_superuser,
                        'last_login': sw.ums_last_login,
                        'date_joined': sw.ums_date_joined
                    }),
                    'message': sw.sms_200,
                    'token': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'access': sw.ts_access_token,
                        'refresh': sw.ts_refresh_token
                    }),
                    'access_token': sw.access_token,
                    'refresh_token': sw.refresh_token
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            )
        }
    )
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': "Already logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response(
                {
                    "user": serializer.data,
                    "message": "register success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK
            )
            response.set_cookie("access", access_token)
            response.set_cookie("refresh", refresh_token)

            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    @swagger_auto_schema(
        operation_id='User Login',
        operation_description='User Login',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': sw.ums_email,
                'password': sw.ums_password
            },
            required=['email', 'password']
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'id': sw.ums_id,
                        'password': sw.ums_password,
                        'email': sw.ums_email,
                        'name': sw.ums_name,
                        'gender': sw.ums_gender,
                        'is_staff': sw.ums_is_staff,
                        'is_superuser': sw.ums_is_superuser,
                        'last_login': sw.ums_last_login,
                        'date_joined': sw.ums_date_joined
                    }),
                    'message': sw.sms_200,
                    'token': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'access': sw.ts_access_token,
                        'refresh': sw.ts_refresh_token
                    }),
                    'access_token': sw.access_token,
                    'refresh_token': sw.refresh_token
                })
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                'Failed', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_400
                })
            )
        }
    )
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': "Already logged in user"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            email=request.data.get("email"),
            password=request.data.get("password")
        )
        if user:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response(
                {
                    "user": serializer.data,
                    "message": "Login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            response.set_cookie("access", access_token)
            response.set_cookie("refresh", refresh_token)
            return response
        return Response({'message': "Account that does not exist or password is not correct"},
                        status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='User Logout',
        operation_description='User Logout',
        responses={
            status.HTTP_202_ACCEPTED: openapi.Response(
                'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'message': sw.sms_202,
                })
            ),
        }
    )
    def delete(self, request):
        if request.user.is_authenticated:
            response = Response({
                "message": "Logout succcess",
                },
                status=status.HTTP_202_ACCEPTED
            )
            response.delete_cookie("access")
            response.delete_cookie("refresh")
            return response
        return Response({'message': "You are not a logged in user"}, status=status.HTTP_400_BAD_REQUEST)
