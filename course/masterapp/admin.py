from django.contrib import admin
from masterapp.models import Category, FinanceCourse, BasePageInfo, FinanceCourseLable

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
   pass

@admin.register(FinanceCourse)
class AdminFinanceCourse(admin.ModelAdmin):
   pass

@admin.register(FinanceCourseLable)
class AdminFinanceCourseLable(admin.ModelAdmin):
   pass

@admin.register(BasePageInfo)
class AdminBasePageInfo(admin.ModelAdmin):
   pass
