from rest_framework import serializers
from django.contrib.auth.models import User
from student.models import Student   # import your Student model


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # extra fields for Student model
    phone = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'city')

    def create(self, validated_data):
        # remove phone from validated_data
        phone = validated_data.pop('phone', "")
        # remove city from validated_data
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
