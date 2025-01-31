from rest_framework import serializers

from userauths.models import User,Profile


#this serilizer convert django model instances into dictonaries which can later be converted in JSON
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ProfileSerializers(serializers.ModelSerializer):
    model=Profile
    fields='__all__'