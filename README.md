# try-django-admin-cookbook

A Django project which deals with customizing Django Admin Interface. It is impressed from https://books.agiliq.com/projects/django-admin-cookbook/en/latest/ and uses similar/different kind of examples. 

> To read colourful documentation visit [https://hygull.github.io/try-django-admin-cookbook/](https://hygull.github.io/try-django-admin-cookbook/). 
>
>The purpose of this project is to learn by making mistakes so don't think about model's structure first time as later it has been enhanced. 
>
>Please focus on how it flows and changes as we advance.

+ First have a look at this docs first.

	+ [1.md](./docs/command_history/1.md)

	+ [2.md](./docs/command_history/2.md)

	+ [3.md](./docs/command_history/3.md)

	+ [4.md](./docs/command_history/4.md)

	+ [5.md](./docs/command_history/5.md)

    + [6.md](./docs/command_history/6.md)

## Defining models, applicaton registry, changing default site texts

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
    first_name = models.CharField(max_length=50, null=False, blank=False, help_text="User's first name")
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
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Who posted?")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Post created at")
    updated_at = models.DateTimeField(auto_now=True, help_text="Post last updated at")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Post belongs to")
    active = models.BooleanField(default=True, help_text="Active status")

    def __str__(self):
        return "Post - {0} by {1}".format(self.pk, self.posted_by.first_name)

```

+ Now, **makemigrations** & **migrate**.

+ Add following to **users/admin.py**.

```python
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
```

+ Now add following to **posts/admin.py**.

```python
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
```

+ Runserver `python manage.py runserver` and check. Now you can see your apps in admin interface.

+ You will be seeing **Categorys** in the page, so just update the Category model by adding Meta class. And it will change **Categorys** to **Categories**.

```python
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Name of category")
    description = models.TextField(default='', help_text="Description of category")

    def __str__(self):
        return "Category - {0}".format(self.pk)

    class Meta:
        verbose_name_plural = "Categories"
```

### Two separate admin sites (for users & posts)

+ Append the following code in **users/admin.py** (very bottom).

```python
# *---* Separate Admin site *---*
class UserAdminSite(admin.AdminSite):
    site_header = "User Admin Site"
    site_title = "Users"
    index_title = "Users list"

users_admin_site = UserAdminSite(name="users-admin-site")
users_admin_site.register(User)
users_admin_site.register(Address)

```

+ Now, append the following code in **posts/admin.py** (very bottom).

```python
# *---* Separate Admin site *---*
class PostAdminSite(admin.AdminSite):
    site_header = "Post Admin Site"
    site_title = "Posts"
    index_title = "Posts list"

posts_admin_site = PostAdminSite(name="posts-admin-site")
posts_admin_site.register(Post)
posts_admin_site.register(Category)

```

+ Open **cookbook/urls.py**, add first 2 import at very top 

```python
from users.admin import users_admin_site
from posts.admin import posts_admin_site
```

+ And then only change **urlpatterns** to

```python
urlpatterns = [
    path('admin/', admin.site.urls),

    # After defining the following 2 patterns, you won't be able to access 
    # default home(/) page. Need to design our own custom home(/) page
    path('users-admin/', users_admin_site.urls),
    path('posts-admin/', posts_admin_site.urls),
]

```

# References 

+ https://books.agiliq.com/en/latest/

+ [https://books.agiliq.com/projects/django-admin-cookbook/en/latest/](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)

+ [Change site header, site title, index title](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html)

+ [Set plural text for model](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/plural_text.html)

+ [Create 2 independent admin sites](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/two_admin.html)

