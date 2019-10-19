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
#router.register(r'tchr',views.TeacherModelViewset)
#router.register(r'rsc', views.ResourceModelViewset)
#router.register(r'rat',views.RatingModelViewset)
#router.register(r'cmnt',views.CommentModelViewset)
#router.register(r'my_links',views.my_links, base_name='MyLinks')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('get_resources/',views.get_resources, name='get_resources'),
    path('get_teachers/',views.get_teachers, name='get_teachers'),
    path('get_create_resource/',views.get_create_resource, name='get_create_resource'),
    path('get_create_ratings/', views.get_create_ratings, name='get_create_ratings'),
    path('get_create_comments/',views.get_create_comments, name='get_create_comments'),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('un/', views.un, name='un'),
    path('logout/',views.user_logout, name='logout'),

    path('set_retrieve_role/',views.set_retrieve_role, name='set_retrieve_role'),
    path('save_resource/', views.save_resource, name='save_resource'),
    path('follow_author/',views.follow_author, name='follow_author'),
    path('search/', views.search, name='search'),
    path('get_pending/', views.get_pending, name='get_pending'),
    path('navigate/', views.navigate, name='navigate'),
    path('approve_resource/',views.approve_resource, name='approve_resource'),
    path('most_followed/', views.most_followed, name='most_followed'),
    path('create_topic/',views.create_topic, name='create_topic'),
    path('get_featured/', views.get_featured, name='get_featured'),
    path('sort_resources/',views.sort_resources, name='sort_resources'),
    path('get_topics/', views.get_topics, name='get_topics'),
    path('get_levels/', views.get_levels, name='get_levels'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
    path('sign_me_in/',views.sign_me_in, name='sign_me_in'),
    
    
]
