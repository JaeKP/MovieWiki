from rest_framework.decorators import api_view
from django.contrib.auth import logout 
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer, UserProfileUpdateSerializer
from rest_framework import status

User = get_user_model()

@api_view(['GET', 'PUT', 'DELETE'])
def user_profile_or_update_or_delete(request, username):
    user = get_object_or_404(User, username=username)
    def user_profile():
        serializers = UserProfileSerializer(user)
        return Response(serializers.data)

    def user_update():
        if request.user == user:
            serializers = UserProfileUpdateSerializer(
                instance=user, data=request.data
            )
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                return Response(serializers.data)

    # def user_delete():
    #     if request.user == user:
    #         request.user.delete()
    #         logout(request)
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return user_profile()
    elif request.method == 'PUT':
        return user_update()
    # elif request.method == 'DELETE':
    #     return user_delete()