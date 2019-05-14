from django.contrib import admin
from posts.models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = [
		"pk",
		"title",
		"active",
		"posted_by",
		"created_at",
		"updated_at"
	]

	search_fields = [
		"pk",
		"title",
		"active"
	]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	search_fields = [
		"pk",
		"name"
	]