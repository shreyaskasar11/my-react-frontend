from django.urls import path
from . import views

urlpatterns = [
    # Course URLs
    path('api/courses/', views.CourseListCreateView.as_view(), name='course_list_create'),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    
    # Instance URLs
    path('api/instances/', views.InstanceListCreateView.as_view(), name='instance_list_create'),
    path('api/instances/<int:year>/<int:semester>/', views.InstanceListView.as_view(), name='instance_list'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>/', views.InstanceDetailView.as_view(), name='instance_detail'),
]
