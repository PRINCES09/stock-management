from django.contrib import admin
from .models import Course,Staff,Student,Book

# Register your models here.
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Book)

admin.site.site_header='Stock Management System'

