from django.db import models
from posts.models import Post

class Address(models.Model):
	city = models.CharField(max_length=50, default='', help_text="User's village name")
	village = models.CharField(max_length=50, default='', help_text="User's city name")
	district = models.CharField(max_length=50, null=True, help_text="User's district name")
	state = models.CharField(max_length=50, blank=True, help_text="User's state name")

	def __str__(self):
		return "Address - {0}".format(self.pk)

class User(models.Model):
	first_name = models.CharField(max_length=50, null=False, blank=False, help_text="User's fisrt name")
	last_name = models.CharField(max_length=50, null=False, blank=False, help_text="User's last name")
	date_of_birth = models.DateField(help_text="User's date of birth")
	address = models.ForeignKey(Address, on_delete=models.CASCADE, help_text="User's address")
	posts = models.ForeignKey(Post, on_delete=models.CASCADE, help_text="User's posts")

	def __str__(self):
		return "User {0}".format(self.pk)



