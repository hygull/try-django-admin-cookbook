from django.contrib import admin
from users.models import User, Address

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = [
		"pk",
		"first_name",
		"last_name",
		"date_of_birth",
		"created_at",
		"updated_at",
		"active"
	]
	search_fields = [
		"pk",
		"first_name",
		"last_name"
	]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	search_fields = [
		"pk",
		"city",
		"village",
		"district",
		"state"
	]

# *---* Separate Admin site *---*
class UserAdminSite(admin.AdminSite):
	site_header = "User Admin Site"
	site_title = "Users"
	index_title = "Users list"

users_admin_site = UserAdminSite(name="users-admin-site")
users_admin_site.register(User)
users_admin_site.register(Address)
