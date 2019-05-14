from django.db import models
from users.models import User


class Category(models.Model):
	name = models.CharField(max_length=50, help_text="Name of category")
	description = models.TextField(default='', help_text="Description of category")

	def __str__(self):
		return "Category - {0}".format(self.pk)
		

class Post(models.Model):
	title = models.CharField(max_length=50, default='', help_text="Post's title")
	description = models.TextField(help_text="Post's description")
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Posted by (Who posted this post)")
	created_at = models.DateTimeField(auto_now_add=True, help_text="Post created at")
	updated_at = models.DateTimeField(auto_now=True, help_text="Post last updated at")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Post belongs to")
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Post - {0} by {1}".format(self.pk, self.posted_by.first_name)


