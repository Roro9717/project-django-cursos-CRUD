from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})


def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalle.html', {'curso': curso})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect('cursos:detalle', pk=curso.pk)
    else:
        form = CursoForm()
    return render(request, 'cursos/formulario.html', {'form': form, 'titulo': 'Crear Curso'})


def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalle', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/formulario.html', {'form': form, 'titulo': 'Editar Curso', 'curso': curso})


def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:lista')
    return render(request, 'cursos/confirmar_eliminar.html', {'curso': curso})
