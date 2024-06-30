from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.create_users, name='register'),
    path('users/<int:user_id>/', views.get_user, name='get-users'), 
    path('users-delete/<int:user_id>/', views.delete_user, name='delete-users'),
    path('users-list', views.users_list, name='users_list'),
    path('users-update/<int:user_id>/', views.update_user, name='update-users'),
    path('users/login/', views.login, name='login'),
]