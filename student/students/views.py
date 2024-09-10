from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Class
from .forms import StudentForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def student_list(request):
    students = Student.objects.all()
    
    # Pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)

    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def admin_dashboard(request):
    total_students = Student.objects.count()
    total_classes = Class.objects.count()
    
    context = {
        'total_students': total_students,
        'total_classes': total_classes,
    }
    return render(request, 'students/admin_dashboard.html', context)

def export_student_pdf(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_details.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Student Name: {student.name}")
    p.drawString(100, 780, f"Roll Number: {student.roll_number}")
    p.drawString(100, 760, f"Email: {student.email}")
    p.drawString(100, 740, f"Enrolled Class: {student.enrolled_class}")

    p.showPage()
    p.save()

    return response
