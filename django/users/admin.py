from django.contrib import admin
from users.models import User, Role

# Register your models here.
# admin.site.register(User)
admin.site.register(Role)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'email', 'username', 'address', 'first_name'