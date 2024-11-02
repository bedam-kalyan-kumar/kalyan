from django.contrib import admin
from django.urls import path
from .views import facebook,instagram,twitter,many,home_page,whatsapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kalyan/',home_page,name="home_page"),
    path('facebook/',facebook,name="facebook"),
    path('twitter/',twitter,name="twitter"),
    path('instagram/',instagram,name="instagram"),
    path('whatsapp/',whatsapp,name="whatsapp"),
    path('',many,name="many"),
]