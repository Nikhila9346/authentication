from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #all data is validated
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'error': "Something went wrong"
            }
            return render(request, 'signup.htm', context)

    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')
 
def home(request):
    return render(request, 'home.html')
    
'''
# Create your views here.
def signup(request):
    #if the user has already logged in then don't allow to the signup or login page
    if request.user.is_authenticated:
        return redirect('home') 
    
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            #if the username already exits return error
            if User.objects.filter(username=username).exists():
                context = {
                    'error': 'Username already exits!!!'
                }
                return render(request, 'signup.html', context)
            else:
                #create_user() -- creates a user where the password will be encrypted
                User.objects.create_user(
                    username = username,
                    password = password1,
                )
                #or store the details of the user in an object and make use of that object to set password
                #ob1 = User.objects.create() then ob1.set_password(password1) then ob1.save()
                return redirect('login.html')
        else:
            context = {
                'error': 'Password does not match!!!'
            }
            return render(request, 'signup.html', context)

    return render(request, 'signup.html')


def login_user(request):
    #if user is already logged in then not needed to allow him to login page
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context={
                'error': "Username or password does not match"
            }
            return render(request, 'login.html', context)
    
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
    

# def home(request):
#     #don't allow the user to go to home page if user is not authenticated
#     if not request.user.is_authenticated:
#         return redirect('login')
#     #if authenticated allow user to home page
#     return render(request, 'home.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
'''