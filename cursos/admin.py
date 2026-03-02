from django.contrib import admin
from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'instructor', 'duracion', 'creado')
    search_fields = ('nombre', 'instructor')
