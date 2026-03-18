from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            course=course
        )
        return redirect('/')

    return render(request, 'index.html')