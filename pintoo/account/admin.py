from django.contrib import admin

from account.models import UserProfile


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'sex', 'lavel']
 
    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileModelAdmin)