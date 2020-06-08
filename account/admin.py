from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ['email', 'username', 'full_name', 'date_joined', 'last_login', 'is_admin', 'is_staff']
	readonly_fields = ('date_joined', 'last_login')
	search_fields = ('email', 'username')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)