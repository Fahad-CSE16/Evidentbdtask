from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("this called")
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
            print(user)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None