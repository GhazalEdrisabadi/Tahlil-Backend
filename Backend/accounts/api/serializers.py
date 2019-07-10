from django.contrib.auth.hashers import get_hasher, identify_hasher, is_password_usable
from django.db.models import Q
from rest_framework import serializers

from rest_framework.serializers import (
    CharField,
    EmailField,
    ImageField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

from accounts.models import Tailor


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = Tailor
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = Tailor
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'Photo',
            'Address',
            'Evidence',
            'WorkExprience',
            'password',

        ]
        extra_kwargs = {"password": {"write_only": True},
                        }

        def validate(self, data):
            username = data['username']
            user_qs = Tailor.objects.filter(username=username)
            if user_qs.exists():
                raise ValidationError("This user has already registered.")
            return data

        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user_obj = Tailor(
                username=username,
                email=email
            )
            user_obj.set_password(password)
            user_obj.save()
            return validated_data

        # def validate_email(self, value):
        #     data = self.get_initial()
        #     email1 = data.get("email2")
        #     email2 = value
        #     if email1 != email2:
        #         raise ValidationError("Emails must match.")
        #
        #     user_qs = Tailor.objects.filter(email=email2)
        #     if user_qs.exists():
        #         raise ValidationError("This user has already registered.")
        #
        #     return value
        #
        # def validate_email2(self, value):
        #     data = self.get_initial()
        #     email1 = data.get("email")
        #     email2 = value
        #     if email1 != email2:
        #         raise ValidationError("Emails must match.")
        #     return value

    def check_password(password, encoded, setter=None, preferred='default'):
        if password is None or not is_password_usable(encoded):
            return False

        preferred = get_hasher(preferred)
        try:
            hasher = identify_hasher(encoded)
        except ValueError:
            return False
