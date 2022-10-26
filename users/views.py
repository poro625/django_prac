import email
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        email =  request.POST.get('email') #이메일
        username =  request.POST.get('username') # 유저네임
        nickname =  request.POST.get('nickname') # 닉네임
        password =  request.POST.get('password') # 비밀번호
        password2 =  request.POST.get('password2') # 비밀번호 확인

        if password == password2:
            User.objects.create_user(email=email, username=username, nickname=nickname, password=password)

            return render(request, 'home.html')
        
        else :

            return render(request, 'signup.html')

    else :

        return HttpResponse('허용되지 않은 메소드 입니다')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password =  request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            loginsession(request, user)

        return render(request ,'home.html' )
    else:
        return HttpResponse('로그인 실패')

def home(request):
    return render(request, 'home.html')


def logout(request): # 로그아웃

    if request.method == 'POST':        
        auth.logout(request)
        redirect('users:home')

    return render(request,'login.html')

def delte(request): # 회원탈퇴
    
    if request.user.is_authenticated:
        request.user.delete()
    return render(request, 'signup.html')

def password(request, id): # 비밀번호 변경    

    if request.method == 'GET':
        return render(request, 'password.html' )

    elif request.method == 'POST':
        user = User.objects.get(id = id)
        user.password = request.POST['password']
        user.set_password(user.password)
        user.save()
        context = {

            'user' : user

        }
        
        return render(request, 'login.html', context)

def detail(request, id): # 회원정보 변경
    if request.method == 'GET':
        return render(request, 'detail.html')

    elif request.method == 'POST':
        user = User.objects.get(id=id)
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.nickname = request.POST.get('email')
        user.save()
        context = {
            'user':user

        }
        return render(request, 'login.html', context)