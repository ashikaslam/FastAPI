
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
import cloudinary.uploader


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'bio', 'profile_image', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        image_file = validated_data.pop('profile_image', None)

        # Upload image if provided
        profile_image_url = None
        if image_file:
            profile_image_url = upload_profile_image_to_cloudinary(image_file)

        username = validated_data['email']
        user = User(username=username, **validated_data)
        user.set_password(password)
        if profile_image_url:
            user.profile_image = profile_image_url
        user.save()
        return user




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        attrs['user'] = user
        return attrs
    


def upload_profile_image_to_cloudinary(image_file):
    response = cloudinary.uploader.upload(image_file, folder="user_profiles")
    return response.get("secure_url")
