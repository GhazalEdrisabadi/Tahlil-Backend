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
