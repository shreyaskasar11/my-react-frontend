from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.title} ({self.year} - Semester {self.semester})"
