from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, TestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserCreate(APIView):
    """ 
    Creates the user. 
    """ 

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    """ 
    Login the user. 
    """

    def get(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                # token = Token.objects.create(user=user)
                # json = serializer.data
                # json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetGroups(APIView):

    def get(self, request, format='json'):
        serializer = TestSerializer(request.user)
        if request.user.is_authenticated:
            json = serializer.data
            #ans = request.user.groups.values_list('id', flat=True)
            ans = json
            return Response(ans)
        else:
            ans = 'False'
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)