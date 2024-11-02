# admin.py
from django.contrib import admin
from .models import MyModel  # Replace MyModel with your model's name

# Register your models here
admin.site.register(MyModel)  # Register the model for admin panel access
