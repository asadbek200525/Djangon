from django.contrib import admin
from myfiles.models import Teacher,fanlar
# Register your models here.

class AdminTeacher(admin.ModelAdmin):
    list_display = ['id','ism','fam','yosh','brithday','fan']

admin.site.register(Teacher,AdminTeacher)

class Adminfan(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(fanlar,Adminfan)
