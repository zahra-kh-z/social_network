from django.contrib import admin
from user.models import Profile
from user.models import Relationship

# Register your models here.
admin.site.register(Relationship)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

