from django.conf import settings
from djanfo.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from service_access.models import ServiceUser




"""
Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

Use the login name and a hash of the password. For example:

ADMIN_LOGIN = 'admin'
ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
"""