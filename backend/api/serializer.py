from rest_framework import serializers

from userauths.models import User,Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#this serilizer convert django model instances into dictonaries which can later be converted in JSON

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)

        token['username']=user.username
        token['email']=user.email
        # if cause error remove it later
        token['full_name']=user.full_name

        return token

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ProfileSerializers(serializers.ModelSerializer):
    model=Profile
    fields='__all__'