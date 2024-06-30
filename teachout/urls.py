from django.contrib import admin
from django.urls import path, include
from user import views 
from user.views import index

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('users/', include('user.urls', namespace='users')),
    path('home/', index) 
]
