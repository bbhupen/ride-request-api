from django.contrib import admin

# Register your models here.

from .models import Request, Driver
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# admin.site.register(Post)
# admin.site.register(Requests)
# admin.site.register(Drivers)

class DriverInline(admin.StackedInline):
    model = Driver
    can_delete = False

class customUserAdmin (UserAdmin):
    inlines = (DriverInline, )
    
admin.site.register(Request)
admin.site.register(Driver)
admin.site.unregister(User)
admin.site.register(User, customUserAdmin)
