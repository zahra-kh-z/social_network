from django.contrib import admin
from user.models import User
from user.models import Relationship

# Register your models here.
# admin.site.register(User)
admin.site.register(Relationship)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
