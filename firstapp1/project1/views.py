from django.shortcuts import render, redirect,get_object_or_404
from .models import login
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        gmail=request.POST.get('gmail')
        # Check if user already exists
        if not login.objects.filter(username=username).exists():
            login.objects.create(username=username , password=password)
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
    # Handle GET request for logged-in users
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        if user_id:
            user = login.objects.filter(id=user_id).first()
            if user:
                return render(request, 'loginsuccess.html', {
                    'username': user.username,
                    'image_url': user.image.url if user.image else None
                })
        return redirect('loginform')  # Redirect to login if not logged in

    # Handle POST request for login
    if request.method == 'POST':
        username = request.POST.get('username')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')

        user = login.objects.filter(
            Q(username=username) | Q(gmail=gmail),
            password=password
        ).first()

        if user:
            request.session['user_id'] = user.id  # Store user ID in session
            return render(request, 'loginsuccess.html', {
                'username': user.username,
                'image_url': user.image.url if user.image else None
            })
        else:
            return render(request, 'loginform.html', {'error': 'Invalid credentials'})

    return redirect('loginform')  # Redirect to login if method is invalid

def search(request):
    return render(request, 'search.html')

def notifications(request):
    return render(request, 'notifications.html')

from .models import login  # Import your custom login model

def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = login.objects.filter(id=user_id).first()
        if user:
            username = user.username or 'Unknown User'
            image_url = user.image.url if user.image else None
        else:
            username = 'User Not Found'
            image_url = None
    else:
        username = 'Not Logged In'
        image_url = None

    return render(request, 'profile.html', {'username': username, 'image_url': image_url})
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
            post.user = request.user  # Associate the post with the logged-in user
            post.save()
            return redirect('profile')  # Redirect to the profile page after upload
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
def index(request):
    return render(request, 'profile.html') 
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
@login_required
def delete_post(request, post_id):
    post = login.objects.get(id=post_id)
    if post.user == request.user:  # Ensure the post belongs to the logged-in user
        post.delete()
    return redirect('profile')

