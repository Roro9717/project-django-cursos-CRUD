from django.test import TestCase
from django.urls import reverse
from .models import Curso


class CursoModelTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            nombre='Python para principiantes',
            descripcion='Aprende Python desde cero',
            duracion=40,
            instructor='Ana García',
        )

    def test_str(self):
        self.assertEqual(str(self.curso), 'Python para principiantes')

    def test_get_absolute_url(self):
        url = self.curso.get_absolute_url()
        self.assertEqual(url, reverse('cursos:detalle', args=[self.curso.pk]))


class CursoViewsTest(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            nombre='Django avanzado',
            descripcion='Técnicas avanzadas de Django',
            duracion=60,
            instructor='Carlos López',
        )

    def test_lista_cursos(self):
        response = self.client.get(reverse('cursos:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django avanzado')

    def test_detalle_curso(self):
        response = self.client.get(reverse('cursos:detalle', args=[self.curso.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django avanzado')

    def test_detalle_curso_no_existe(self):
        response = self.client.get(reverse('cursos:detalle', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_crear_curso_get(self):
        response = self.client.get(reverse('cursos:crear'))
        self.assertEqual(response.status_code, 200)

    def test_crear_curso_post(self):
        data = {
            'nombre': 'HTML y CSS',
            'descripcion': 'Fundamentos web',
            'duracion': 20,
            'instructor': 'María Torres',
        }
        response = self.client.post(reverse('cursos:crear'), data)
        self.assertEqual(Curso.objects.count(), 2)
        nuevo = Curso.objects.get(nombre='HTML y CSS')
        self.assertRedirects(response, reverse('cursos:detalle', args=[nuevo.pk]))

    def test_crear_curso_post_invalido(self):
        response = self.client.post(reverse('cursos:crear'), {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Curso.objects.count(), 1)

    def test_editar_curso_get(self):
        response = self.client.get(reverse('cursos:editar', args=[self.curso.pk]))
        self.assertEqual(response.status_code, 200)

    def test_editar_curso_post(self):
        data = {
            'nombre': 'Django avanzado actualizado',
            'descripcion': 'Contenido actualizado',
            'duracion': 80,
            'instructor': 'Carlos López',
        }
        response = self.client.post(reverse('cursos:editar', args=[self.curso.pk]), data)
        self.assertRedirects(response, reverse('cursos:detalle', args=[self.curso.pk]))
        self.curso.refresh_from_db()
        self.assertEqual(self.curso.nombre, 'Django avanzado actualizado')

    def test_eliminar_curso_get(self):
        response = self.client.get(reverse('cursos:eliminar', args=[self.curso.pk]))
        self.assertEqual(response.status_code, 200)

    def test_eliminar_curso_post(self):
        response = self.client.post(reverse('cursos:eliminar', args=[self.curso.pk]))
        self.assertRedirects(response, reverse('cursos:lista'))
        self.assertEqual(Curso.objects.count(), 0)

    def test_home_redirects_to_lista(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('cursos:lista'))
