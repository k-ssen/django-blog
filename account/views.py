from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password )
            if user is not None:
                login(request, user)
                return redirect("/")

    else:
        form =  LoginForm()
        return render(request, "account.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("list")

def register_view(request):
    #우리가 폼으로 받은 데이터로 유저를 만들어야하기 때문이다
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            #만약 회원가입 하자마자 로그인 상태가 되기를 원한다면,
            login(request, user)
            return redirect("list")
        return render(request, "account.html", {"form": form})

    else:
        form =  RegisterForm()
        return render(request, "account.html", {"form": form})