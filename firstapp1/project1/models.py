from django.db import models

class login(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile_photos/', blank=True, null=True)  # Profile photo
    created_at = models.DateTimeField(auto_now_add=True)  # Optional: track user creation
    gmail = models.EmailField(max_length=254)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(login, on_delete=models.CASCADE)  # Link to the `login` model
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} ({self.id})"
