from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True, 'required' : True}}

#    def create(self, validate_data):
#        user = User.objects.create_user(**validate_data) # When you use "validate_data" is means that the
#                                                         # password will be hashed and not raw string
#        return user
# 