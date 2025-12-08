from rest_framework import serializers
from django.contrib.auth.models import User
from student.models import Student


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # extra fields for Student model
    phone = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'city')

    def create(self, validated_data):
        phone = validated_data.pop('phone', "")
        city = validated_data.pop('city', "")

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        Student.objects.create(
            user=user,
            phone=phone,
            city=city
        )

        return user
