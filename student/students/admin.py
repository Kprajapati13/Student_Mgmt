from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student, Class, Subject, Grade

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(ImportExportModelAdmin):
    pass
