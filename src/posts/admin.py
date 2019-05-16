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

# *---* Separate Admin site *---*
class PostAdminSite(admin.AdminSite):
	site_header = "Post Admin Site"
	site_title = "Posts"
	index_title = "Posts list"

posts_admin_site = PostAdminSite(name="posts-admin-site")
posts_admin_site.register(Post)
posts_admin_site.register(Category)
