# myApp/backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.MultipleObjectsReturned:
            # If multiple users are found, return None or handle it accordingly
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            plaintext_password = 'password'
            if user.check_password(plaintext_password):
                print('Password is correct')
            else:
                print('Password is incorrect')
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class AdminBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            admin = User.objects.get(Q(email=username) & Q(is_staff=True))
            if admin.check_password(password):
                return admin
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
