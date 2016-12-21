from django.contrib import admin
from .models import Category, Course_detail, CourseImage, MainCategory, CategoryImage

# Register your models here.

admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(CategoryImage)
admin.site.register(Course_detail)
admin.site.register(CourseImage)

