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
from users.admin import users_admin_site
from posts.admin import posts_admin_site
from django.contrib.auth.models import User, Group

# Admin Interface: change site-header, site-title & index-title 
admin.site.site_header = "Admin Interface Cookbook"
admin.site.site_title = "Customizing Admin Interface"
admin.site.index_title = "Apps and related models"

# Hide User & Group from admin (/admin/)
admin.site.unregister(User)
admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),

    # After defining the following 2 patterns, you won't be able to access 
    # default home(/) page. Need to design our own custom home(/) page
    path('users-admin/', users_admin_site.urls),
    path('posts-admin/', posts_admin_site.urls),
]
