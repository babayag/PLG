from rest_framework import serializers
from .models import Lead
from .models import SpaUser
from .models import Payment
from .models import Search
from .models import Forfait
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

"""
    author : Domngang Eric Faycal
    params : 
    description : serializer for create a user
"""
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

"""
    author : Domngang Eric Faycal
    params : 
    description : serializer for user
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
class DetailLead(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
"""
    author : Domngang Eric Faycal
    params : 
    description : serializer for login a user
"""
class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

"""
    author : Ranyl Foumbi and Kevin Ngaleu
    params : 
    description : serializer for load a user
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaUser
        fields = '__all__'

"""
    author : Ranyl Foumbi , Kevin ngaleu
    params : 
    description : serializer for load a payment
"""
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

"""
    author : Ranyl Foumbi , Kevin ngaleu
    params : 
    description : serializer for load forfait
"""
class ForfaitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forfait
        fields = '__all__'

"""
    author : Ranyl Foumbi , Kevin ngaleu
    params : 
    description : serializer for load search of user
"""
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'

