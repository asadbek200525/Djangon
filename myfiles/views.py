from django.shortcuts import render
from myfiles.models import Teacher,fanlar
# Create your views here.

def main(malumot):
    if malumot.method == 'POST':
        name = malumot.POST.get('ism')
        surneme = malumot.POST.get('fam')
        age = malumot.POST.get('yosh')
        brithrday = malumot.POST.get('kun')
        subjects_id = malumot.POST.get('fan')
        subjects = fanlar.objects.get(id=subjects_id)
        Teacher(ism = name,fam=surneme,yosh=age,brithday=brithrday,fan=subjects).save()

    return render(malumot,'asosiy.html')
def teacher(malumot):
    oqituvchilar = Teacher.objects.all()
    lugat = {'salom':oqituvchilar}
    return render(malumot,'teacher.html',lugat)

def add(malumot):
    fan = fanlar.objects.all()
    return render(malumot,'oqtuvchi.html',{'fanlar':fan})