from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('user_page',views.user_page,name="user_page"),
    path('update_details/<int:id>',views.update_details,name="update_details"),
    path('add_user_details',views.add_user_details,name="add_user_details"),
    path('delete_user_details/<int:id>',views.delete_user_details,name="delete_user_details"),
    path('deletecomment/<int:id>',views.deletecomment,name="deletecomment"),
    path('editcomment/<int:id>',views.editcomment,name="editcomment"),
]