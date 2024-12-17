from django.shortcuts import render, redirect
from .models import login
from django.contrib.auth.decorators import login_required
from .models import Post  # Assuming you have a Post model for user posts
from .forms import PostForm  

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user already exists
        if not login.objects.filter(username=username).exists():
            login.objects.create(username=username, password=password)
            return redirect('success')
        else:
            return render(request, 'register.html', {'error': 'Username already exists'})
    
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def loginform(request):
    return render(request, 'loginform.html')

def forget(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        
        # Check if the username exists in the database
        user = login.objects.filter(username=username).first()
        
        if user and user.password != new_password:
            # Update the user's password
            user.password = new_password
            user.save()
            return redirect('success')
        else:
            return render(request, 'forget.html', {'error': 'Enter valid details'})
    
    return render(request, 'forget.html')

def otp(request):
    return render(request, 'otp.html')

def newpass(request):
    return render(request, 'newpass.html')

def loginsuccess(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Custom authentication for non-standard Django User model
        user = login.objects.filter(username=username, password=password).first()
        
        if user:
            # Login successful
            return redirect('loginsuccess')
        else:
            # Invalid login credentials
            return render(request, 'loginform.html', {'error': 'Invalid username or password'})

    return render(request, 'loginsuccess.html')

def search(request):
    return render(request, 'search.html')

def notifications(request):
    return render(request, 'notifications.html')
@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:  # Ensure the post belongs to the logged-in user
        post.delete()
    return redirect('profile')
@login_required
def profile(request):
    
    username = request.session.get('username', 'Guest')
    return render(request, 'profile.html', {'username': username})

def changepass(request):
    return render(request, 'changepass.html')

def messsages(request):
    return render(request, 'messages.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')  # Redirect to profile after post creation
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
def change_profile_photo(request):
    user_id = request.session.get('user_id')  # Get logged-in user's ID
    if not user_id:
        return redirect('loginsuccess')  # Redirect to login if not logged in

    user = login.objects.filter(id=user_id).first()
    if request.method == 'POST' and user:
        profile_photo = request.FILES.get('profile_photo')  # Get the uploaded file
        if profile_photo:
            user.image = profile_photo  # Update the image field
            user.save()  # Save changes to the database
            return redirect('profile')  # Redirect to profile page

    return render(request, 'change_profile_photo.html', {'user': user})