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




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
