from django.contrib import admin
from django.urls import path
from .views import (
    loginform, forget, otp, newpass, register, success,create_post,delete_post,
    loginsuccess, search, notifications, profile, changepass, messsages,change_profile_photo
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginform, name="loginform"),
    path('forget/', forget, name="forget"),
    path('otp/', otp, name="otp"),
    path('newpass/', newpass, name='newpass'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    path('loginsuccess/', loginsuccess, name='loginsuccess'),
    path('search/', search, name='search'),
    path('notifications/', notifications, name='notifications'),
    path('profile/', profile, name='profile'),
    path('changepass/', changepass, name='changepass'),
    path('messages/', messsages, name='messages'),
    path('change_profile_photo/', change_profile_photo, name='change_profile_photo'),
    path('create_post/',create_post, name='create_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
