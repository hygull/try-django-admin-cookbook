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