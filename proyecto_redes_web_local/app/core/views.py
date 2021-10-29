from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def Login (request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']

        user_auth = authenticate(request, username=user, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, f'Bienvenido {request.user}!')
            return redirect('info')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto, vuelva a intentarlo!!!')

    return render (request, 'login/login.html')

def Logout (request):
    user = request.user
    logout(request)
    messages.success(request, f'Vuelva pronto {user} !!')

    return redirect ('login')

@login_required(login_url='login')
def Info (request):
    return render (request, 'info/info.html')
