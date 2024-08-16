from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Course, CourseInstance
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class CourseListCreateView(View):
    def get(self, request, *args, **kwargs):
        courses = list(Course.objects.values())
        return JsonResponse(courses, safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        course = Course.objects.create(
            title=data['title'],
            code=data['code'],
            description=data['description']
        )
        return JsonResponse({'id': course.id}, status=201)

class CourseDetailView(View):
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        return JsonResponse({
            'title': course.title,
            'code': course.code,
            'description': course.description
        })

    @method_decorator(csrf_exempt)
    def delete(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        course.delete()
        return JsonResponse({}, status=204)

class InstanceListCreateView(View):
    def get(self, request, *args, **kwargs):
        instances = list(CourseInstance.objects.values())
        return JsonResponse(instances, safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        instance = CourseInstance.objects.create(
            year=data['year'],
            semester=data['semester'],
            course_id=data['course_id']
        )
        return JsonResponse({'id': instance.id}, status=201)

class InstanceListView(View):
    def get(self, request, year, semester, *args, **kwargs):
        instances = list(CourseInstance.objects.filter(year=year, semester=semester).values())
        return JsonResponse(instances, safe=False)

class InstanceDetailView(View):
    def get(self, request, year, semester, pk, *args, **kwargs):
        instance = get_object_or_404(CourseInstance, year=year, semester=semester, pk=pk)
        return JsonResponse({
            'year': instance.year,
            'semester': instance.semester,
            'course_id': instance.course_id
        })

    @method_decorator(csrf_exempt)
    def delete(self, request, year, semester, pk, *args, **kwargs):
        instance = get_object_or_404(CourseInstance, year=year, semester=semester, pk=pk)
        instance.delete()
        return JsonResponse({}, status=204)
