from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.forms import UserForm, UserProfileForm
from account.models import UserProfile


@login_required
def account(request):
    try:
        if UserProfile.objects.get(user=request.user):
            context = {'account':UserProfile.objects.get(user=request.user)}
            print('doTry')
    except:
        print('doExcept')
        context={}
    print(context)
    return render(request, 'account/account.html', context) 

def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm(),})
    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm,})
    user = userForm.save()
    userProfile = UserProfile()
    userProfile.user = user
    userProfile.name = 'User還未命名'
    userProfile.lavel = 0
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect('account:login')


def login(request):
    '''
    Login an existing user
    '''
    
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template, {'nextURL':request.GET.get('next')})
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)
    if not user.is_active:
        messages.error(request, '帳號已停用')
        return render(request, template)
    # login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:main')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('account:login') 
