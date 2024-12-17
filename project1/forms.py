from django import forms
from .models import login, Post

# Form for user registration
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['username', 'password', 'gmail']
        widgets = {
            'password': forms.PasswordInput(),  # Password input should be hidden
        }

# Form for creating posts (images/videos)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Correctly reference the Post model
        fields = ['caption', 'image', 'video']  # Use fields from the Post model