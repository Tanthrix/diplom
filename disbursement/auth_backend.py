from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import UserRole, Role

class AdminOnlyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                # Проверяем, есть ли у пользователя роль "admin"
                if UserRole.objects.filter(user=user, role__role_name='admin').exists():
                    return user
                else:
                    return None
            else:
                return None
        except UserModel.DoesNotExist:
            return None