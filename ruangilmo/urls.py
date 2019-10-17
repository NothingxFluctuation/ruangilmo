"""ruangilmo URL Configuration

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
from django.urls import path, include
from boardapp import views
from rest_framework import routers, permissions

router = routers.DefaultRouter()
router.register(r'tchr',views.TeacherModelViewset)
router.register(r'rsc', views.ResourceModelViewset)
router.register(r'rat',views.RatingModelViewset)
router.register(r'cmnt',views.CommentModelViewset)
#router.register(r'my_links',views.my_links, base_name='MyLinks')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('get_resources/',views.get_resources, name='get_resources'),
    path('get_teachers/',views.get_teachers, name='get_teachers'),
    path('create_resource/',views.create_resource, name='create_resource'),
    path('get_create_ratings/', views.get_create_ratings, name='get_create_ratings'),
    path('get_create_comments/',views.get_create_comments, name='get_create_comments'),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('un/', views.un, name='un'),
    
]
