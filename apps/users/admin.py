from django.contrib import admin
from apps.users.models import *

admin.site.register(CustomUser)
admin.site.register(Role)
