from django.shortcuts import render, redirect
from .forms import UserLoginForm,UserSignUpForm
from .models import Profile
from django.contrib.auth import login, logout


# Create your views here.
def signin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:index')

    return render(request, 'signin.html', {'form': form})

def signup(request):    
    form = UserSignUpForm()
    if request.method =='POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')

    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('main:index')


def new_profile(request):
    #로그인하지 않았다면 프로필 누르더라도 계속 홈으로 이동
    if request.user.is_anonymous:
        return redirect("main:index")

    #로그인 했다면 해당 user 의 profile 보기
    profile, created = Profile.objects.get_or_create(user = request.user)
    return render(request, 'Profile.html', {"profile": profile})
    # get = 이미 존재한다. = created = FALSE
    # create = 존재하지 않는다.  = created = TRUE


def create_profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    if request.method == "POST":
        profile.nickname = request.POST.get('nickname')
        profile.image = request.FILES.get('image')
        profile.save()
        return redirect('user:new_profile')
    #나쁜 사용자
    return render(request, "Profile.html", {'profile':profile})
