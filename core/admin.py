from django.contrib import admin

# Register your models here.


from .models import CustomUser, Task
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Task)
