from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

# from rest_auth.serializers import UserDetailsSerializer
# class UserSerializer(UserDetailsSerializer):
# 
# – USER_DETAILS_SERIALIZER - serializer class in rest_auth.
# views.UserDetailsView, default value rest_auth.serializers.
# UserDetailsSerializer

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password' : {'write_only' : True, 'required' : True}}
# 
#    def create(self, validate_data):
#        user = User.objects.create_user(**validate_data) # When you use "validate_data" is means that the
#                                                         # password will be hashed and not raw string
#        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)

# class UserSerializer(serializers.ModelSerializer):    
#     groups = GroupSerializer(many=True)
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff', 'groups',)

class TestSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
   
    class Meta:
        model = User
        fields = ('id','groups',)