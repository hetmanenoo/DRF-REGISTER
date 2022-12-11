import io
import hashlib
import os

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        data = super(RegisterSerializer, self).validate(attrs)
        if len(data['password']) <= 8:
            raise serializers.ValidationError('Password small')
        else:
            hash_object = hashlib.md5(data['password'].encode('utf-8'))
            data['password'] = hash_object.hexdigest()
        return data

