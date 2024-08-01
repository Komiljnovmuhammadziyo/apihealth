from rest_framework import serializers
from tutorial.quickstart.serializers import UserSerializer

from users.models import CustomUser

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class UserDetailSerializer(serializers.ModelSerializer):
    first = userSerializer(read_only=True)
    last_name = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'




