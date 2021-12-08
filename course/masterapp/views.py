from django.shortcuts import render, redirect 
from masterapp.models import  Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required #декоратор проверяющий залогинен ли пользователь 


@login_required(login_url='auth_page')
def base(request):
    menu = Category.objects.all()
    return render(request, 'masterapp/base.html', {'menu': menu, 'title': 'информация к изучению...'})

def auth_page(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Нам не известен такой человек')
    
    return render(request, 'masterapp/auth_page.html')

def logout_user(request):
    logout(request)
    return redirect(auth_page)

def pageNotFound(request, exception):
    return render(request, 'masterapp/page_not_found.html') 