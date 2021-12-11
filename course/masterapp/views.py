from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from masterapp.models import FinanceCourse 
from masterapp.models import Category, FinanceCourseLable
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required #декоратор проверяющий залогинен ли пользователь 


menu = Category.objects.all()
list_lable = FinanceCourseLable.objects.all()

@login_required(login_url='auth_page')
def base(request):
    context = {
        'menu': menu, 
        'title': 'информация к изучению...'
        }
    return render(request, 'masterapp/base.html', context=context )

@login_required(login_url='auth_page')
def money_intelligence(request):
    context = {
        'list_lable': list_lable,
        'menu': menu, 
        'title': 'денежный интелект'
        }
    return render(request, 'masterapp/money_intelligence.html', context=context )


@login_required(login_url='auth_page')
def course_page(request, post_id):
    try:
        content = FinanceCourse.objects.get(pk=post_id)
        context = {
            'title': 'денежный интелект',
            'content': content,
        }
        return render(request,'masterapp/course_page.html', context=context)
    except Exception as ex:
        print(ex)
        return HttpResponse('<h1>Страницы не существует</h1>')



def auth_page(request):
    if request.user.is_authenticated:
        return redirect('base')
    else:
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