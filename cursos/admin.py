
# Register your models here.
from django.contrib import admin
from .models import Categoria, Curso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha_inicio", "activo", "carga_horaria")
    list_filter = ("activo", "categoria")
    search_fields = ("titulo", "descripcion")
    ordering = ("-fecha_inicio",)