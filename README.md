# try-django-admin-cookbook

A Django project which deals with customizing Django Admin Interface. It is impressed from https://books.agiliq.com/projects/django-admin-cookbook/en/latest/ and uses similar/different kind of examples. 

> To read colourful documentation visit [https://hygull.github.io/try-django-admin-cookbook/](https://hygull.github.io/try-django-admin-cookbook/)

+ First have a look at this docs first.

	+ [1.md](./docs/command_history/1.md)

	+ [2.md](./docs/command_history/2.md)

	+ [3.md](./docs/command_history/3.md)

	+ [4.md](./docs/command_history/4.md)

	+ [5.md](./docs/command_history/5.md)

+ In `cookbook/urls.py`, add the following lines just after import statements

```python
# Admin Interface: change site-header, site-title & index-title 
admin.site.site_header = "Admin Interface Cookbook"
admin.site.site_title = "Customizing Admin Interface"
admin.site.index_title = "Apps and related models"
```

so that it will look like below.

> **Note:** I am not going to paste the whole code next time, this is to make sure my point is clear to you readers only first time. So stay active, stay focused.

```python
"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Admin Interface: change site-header, site-title & index-title 
admin.site.site_header = "Admin Interface Cookbook"
admin.site.site_title = "Customizing Admin Interface"
admin.site.index_title = "Apps and related models"

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

+ Now create 2 apps named **users** and **posts**.

+ Define the following 2 models in **users/models.py**.

```python

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
    created_at = models.DateTimeField(auto_now_add=True, help_text="User created at")
    updated_at = models.DateTimeField(auto_now=True, help_text="User details last updated at")
    active = models.BooleanField(default=True, help_text="Active status")

    def __str__(self):
        return "User {0}".format(self.pk)

```

+ Now, define the following 2 models(including 1 import statement) in **posts/models.py**.

```python
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
    active = models.BooleanField(default=True, help_text="Active status")

    def __str__(self):
        return "Post - {0} by {1}".format(self.pk, self.posted_by.first_name)

```

+ Now, **makemigrations** & **migrate**.



# References 

+ https://books.agiliq.com/en/latest/

+ [https://books.agiliq.com/projects/django-admin-cookbook/en/latest/](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)