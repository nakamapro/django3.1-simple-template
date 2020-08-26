# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class EmailBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class PhoneBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(phone=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(phone=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
