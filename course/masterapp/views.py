from django.shortcuts import render
from masterapp.models import  Category

def base(request):
    menu = Category.objects.all()
    return render(request, 'masterapp/base.html', {'menu': menu, 'title': 'информация к изучению...'})

def auth_page(request):
    return render(request, 'masterapp/auth_page.html')

def pageNotFound(request, exception):
    return render(request, 'masterapp/page_not_found.html')