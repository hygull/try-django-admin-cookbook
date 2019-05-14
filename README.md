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



# References 

+ https://books.agiliq.com/en/latest/

+ [https://books.agiliq.com/projects/django-admin-cookbook/en/latest/](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)