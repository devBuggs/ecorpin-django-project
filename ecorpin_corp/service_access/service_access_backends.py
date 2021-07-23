from django.conf import settings
from djanfo.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from service_access.models import ServiceUser



class ServiceAccessBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """
    def authenticate(self, request, service_id=None, password=None):
        service_user_obj = ServiceUser.objects.filter(service_id = service_id)
        username = None
        if service_user_obj:
            print("----------------->", service_user_obj)
            username = str(service_user_obj.user.username)
            # main backend
            login_valid = (settings.ADMIN_LOGIN == username)
            pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
            if login_valid and pwd_valid:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    # raise a error
                    raise ValidationError("Invalid! pls try again..")
                return user
            return None
        else:
            raise ValueError("Service Id not found! check and try again..")

        
    def get_user(self, user_id):
        try:
            #return User.objects.get(pk=user_id)
            return ServiceUser.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None
