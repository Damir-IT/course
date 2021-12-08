from django.http.response import HttpResponse
from django.shortcuts import render
from masterapp.models import Category, FinanceCourseLable


menu = Category.objects.all()
list_lable = FinanceCourseLable.objects.all()
# список позиций меню сайта

def base(request):
    context = {
        'menu': menu, 
        'title': 'информация к изучению...'
        }
    return render(request, 'masterapp/base.html', context=context )


def money_intelligence(request):
    context = {
        'list_lable': list_lable,
        'menu': menu, 
        'title': 'денежный интелект'
        }
    return render(request, 'masterapp/money_intelligence.html', context=context )

def course_page(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def auth_page(request):
    return render(request, 'masterapp/auth_page.html')


def pageNotFound(request, exception):
    return render(request, 'masterapp/page_not_found.html')