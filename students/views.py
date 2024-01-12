from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

from .forms import StudentForm
from .models import Student
from .your_functions import create_student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save()  # 演示立即写入数据库
            create_student.push(name=form.cleaned_data['name'], age=form.cleaned_data['age'])  # 演示,使用 funboost后台中操作orm写入数据库
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})
