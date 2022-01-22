from imp import IMP_HOOK
from django.contrib import admin
from app.models import TODO

# Register your models here.

admin.site.register(TODO)
